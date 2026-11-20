"""pytest version of BankVerification and the __main__ checks in bank_account.py.

Run from the folder that contains bank_account.py:
    pytest -v test_bank_account.py
"""
from cmath import log
from Python_OOP_polymorphism.Overriding import B
import pytest
from Python_OOP.bank_account import (BankAccount, CheckingAccount, SavingsAccount,
                                     StudentAccount, FlatFee, OverdraftFee, FeeStrategy, FlatRate, TieredRate, LargeWithdrawalAlert, AuditLog)

# Inputs that are not a positive number. Reused by several tests.
INVALID_AMOUNTS = [-100, -0.1, 0, None, "100", "abc", True]


# --------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def reset_class_state(monkeypatch):
    """Runs before EVERY test (autouse=True).

    Class attributes are shared by the whole run. monkeypatch puts the
    original values back after each test, so one test can't leak
    accounts_created or interest_rate into the next one.
    """
    monkeypatch.setattr(BankAccount, "accounts_created", 0)


@pytest.fixture
def luiza():
    return BankAccount("Luiza", 1_000)


@pytest.fixture
def andrew():
    return BankAccount("Andrew", 500)


# --------------------------------------------------------------------------
# Class attributes (was BankVerification.bank_account_check)
# --------------------------------------------------------------------------
def test_accounts_created_counts_every_account(luiza, andrew):
    assert BankAccount.accounts_created == 2


def test_apply_interest_uses_no_rate(luiza):
    luiza.apply_interest()
    assert luiza.balance == 1000
    assert luiza.transactions == []


def test_personal_rate_only_affects_that_account():
    ana = SavingsAccount("Ana", 1000, interest_strategy=FlatRate(0.10))
    john = SavingsAccount("Ana", 500)
    ana.apply_interest()
    john.apply_interest()
    assert ana.balance == 1100
    assert john.balance == 525


# --------------------------------------------------------------------------
# deposit
# --------------------------------------------------------------------------
def test_deposit_single_amount(luiza):
    luiza.deposit(100)
    assert luiza.balance == 1100
    assert luiza.transactions == ["deposit 100"]


def test_deposit_with_note_and_several_amounts():
    a = BankAccount("Ana", 0)
    a.deposit(50)
    a.deposit(100, note="salary")
    a.deposit(10, 20, 30)
    assert a.balance == 210
    assert a.transactions == ["deposit 50", "deposit 100 (salary)",
                              "deposit 10", "deposit 20", "deposit 30"]


@pytest.mark.parametrize("amount", INVALID_AMOUNTS)
def test_deposit_rejects_invalid_amount(luiza, amount):
    with pytest.raises(ValueError, match="greater than 0"):
        luiza.deposit(amount)
    assert luiza.balance == 1000  # a failed operation changes nothing
    assert luiza.transactions == []


def test_deposit_is_all_or_nothing(luiza):
    with pytest.raises(ValueError):
        luiza.deposit(10, -5, 20)
    assert luiza.balance == 1000  # not even the 10 went in
    assert luiza.transactions == []


def test_deposit_without_amounts(luiza):
    with pytest.raises(ValueError, match="No amounts given"):
        luiza.deposit()


# --------------------------------------------------------------------------
# withdraw (was check_bad_withdrawal_transaction)
# --------------------------------------------------------------------------
def test_withdraw_single_amount(luiza):
    luiza.withdraw(50)
    assert luiza.balance == 950
    assert luiza.transactions == ["withdraw 50"]


@pytest.mark.parametrize("amount", INVALID_AMOUNTS)
def test_withdraw_rejects_invalid_amount(luiza, amount):
    with pytest.raises(ValueError, match="greater than 0"):
        luiza.withdraw(amount)
    assert luiza.balance == 1000
    assert luiza.transactions == []


def test_withdraw_more_than_balance(luiza):
    with pytest.raises(ValueError, match="Insufficient balance"):
        luiza.withdraw(1001)
    assert luiza.balance == 1000


def test_withdraw_exact_balance_is_allowed(luiza):
    luiza.withdraw(1000)
    assert luiza.balance == 0


def test_withdraw_without_amounts(luiza):
    with pytest.raises(ValueError, match="No amounts given"):
        luiza.withdraw()


# --------------------------------------------------------------------------
# is_valid_amount (was check_valid_amounts)
# --------------------------------------------------------------------------
@pytest.mark.parametrize("amount, expected", [
    (1000, True),
    (50, True),
    (0.1, True),
    (-5, False),
    (0, False),
    (-0.99, False),
    (None, False),
    ("abc", False),
    ("100", False),
    (True, False),
])
def test_is_valid_amount(amount, expected):
    assert BankAccount.is_valid_amount(amount) is expected


# --------------------------------------------------------------------------
# from_string (was check_inputs_from_string)
# --------------------------------------------------------------------------
@pytest.mark.parametrize("text, message", [
    ("Luiza", "Expected 'owner,balance'"),
    ("Luiza,1000,extra", "Expected 'owner,balance'"),
    ("Luiza,abc", "whole number"),
    (",1000", "Owner name is missing"),
    ("Luiza,-50", "cannot be negative"),
])
def test_from_string_rejects_bad_input(text, message):
    with pytest.raises(ValueError, match=message):
        BankAccount.from_string(text)


def test_from_string_valid_input():
    acc = BankAccount.from_string(" Luiza , 1000 ")
    assert (acc.owner, acc.balance) == ("Luiza", 1000)


def test_from_string_returns_the_subclass():
    acc = SavingsAccount.from_string("Andrew,500")
    assert type(acc) is SavingsAccount
    assert acc.min_balance == 100


def test_from_string_applies_subclass_rules():
    with pytest.raises(ValueError, match="at least 100"):
        SavingsAccount.from_string("Tim,50")


# --------------------------------------------------------------------------
# SavingsAccount
# --------------------------------------------------------------------------
def test_savings_opening_balance_below_minimum():
    with pytest.raises(ValueError, match="at least 100"):
        SavingsAccount("Mara", 50)
    assert BankAccount.accounts_created == 0


def test_savings_can_land_exactly_on_minimum():
    s = SavingsAccount("Mara", 1000)
    s.withdraw(900)
    assert s.balance == 100


def test_savings_cannot_go_below_minimum():
    s = SavingsAccount("Mara", 200)
    with pytest.raises(ValueError, match="Below minimum balance of 100"):
        s.withdraw(101)
    assert s.balance == 200
    assert s.transactions == []


def test_savings_several_withdrawals_checked_together():
    s = SavingsAccount("Mara", 500)
    s.withdraw(100, 150)
    assert s.balance == 250
    with pytest.raises(ValueError, match="Below minimum"):
        s.withdraw(100, 100)  # 250 - 200 = 50 < 100
    assert s.balance == 250


def test_savings_statement():
    assert SavingsAccount("Mara", 200).statement() == "Mara: 200 (savings)"


def test_savings_is_a_bank_account():
    assert isinstance(SavingsAccount("Mara", 200), BankAccount)


def test_savings_month_end_adds_interest():
    s = SavingsAccount("Mara", 1000)
    s.month_end()
    assert s.balance == 1050
    assert s.transactions == ["interest 50.0"]


# --------------------------------------------------------------------------
# CheckingAccount
# --------------------------------------------------------------------------
def test_checking_negative_overdraft_limit_rejected():
    with pytest.raises(ValueError, match="0 or more"):
        CheckingAccount("Ion", 100, overdraft_limit=-50)
    assert BankAccount.accounts_created == 0  # rejected before super().__init__


def test_checking_can_go_exactly_to_overdraft_limit():
    john = CheckingAccount("John", 100)
    john.withdraw(600)
    assert john.balance == -500


def test_checking_cannot_go_past_overdraft_limit():
    john = CheckingAccount("John", 100)
    with pytest.raises(ValueError, match="Overdraft limit exceeded"):
        john.withdraw(601)
    assert john.balance == 100


@pytest.mark.parametrize("withdrawal, expected_fee", [
    (50, 5),  # balance 50: maintenance only
    (150, 15),  # balance -50: maintenance + overdraft penalty
])
def test_checking_month_end_fee(withdrawal, expected_fee):
    ion = CheckingAccount("Ion", 100)
    ion.withdraw(withdrawal)
    ion.month_end()
    assert ion.balance == 100 - withdrawal - expected_fee
    assert ion.transactions[-1] == f"fee {expected_fee}"


# --------------------------------------------------------------------------
# StudentAccount
# --------------------------------------------------------------------------
def test_student_withdraw_under_limit():
    st = StudentAccount("Dan", 1000)
    st.withdraw(150)
    assert st.statement() == "Dan: 850"


def test_student_withdraw_over_limit():
    st = StudentAccount("Dan", 1000)
    with pytest.raises(ValueError, match="Over the withdrawal limit"):
        st.withdraw(300)
    assert st.balance == 1000


def test_student_still_cannot_go_below_zero():
    st = StudentAccount("Ema", 100)
    with pytest.raises(ValueError, match="Insufficient balance"):
        st.withdraw(150)


def test_student_negative_limit_rejected():
    with pytest.raises(ValueError, match="0 or more"):
        StudentAccount("Maria", 1000, max_withdrawal=-50)
    assert BankAccount.accounts_created == 0


def test_student_limit_is_per_withdrawal():
    """Design decision from the review: is max_withdrawal per withdrawal
    or per call? This test says per withdrawal. It FAILS on the current code,
    because withdraw() passes sum(amounts) to _check_funds."""
    st = StudentAccount("Dan", 1000)
    st.withdraw(100, 150)  # each one is under 200
    assert st.balance == 750


# --------------------------------------------------------------------------
# Operators (__eq__, __lt__, __len__)
# --------------------------------------------------------------------------
def test_equal_accounts_are_not_the_same_object():
    a, b = BankAccount("Ana", 100), BankAccount("Ana", 100)
    assert a == b
    assert a is not b


def test_compare_with_non_account_does_not_crash():
    assert (BankAccount("Ana", 100) == "Ana") is False


def test_sorted_orders_by_balance():
    accounts = [BankAccount("Ana", 100), BankAccount("Dan", 50),
                BankAccount("Ion", 75)]
    assert [acc.owner for acc in sorted(accounts)] == ["Dan", "Ion", "Ana"]


def test_less_than_and_greater_than():
    a, c = BankAccount("Ana", 100), BankAccount("Dan", 50)
    assert not a < c
    assert a > c  # Python flips it to c < a


def test_len_counts_transactions():
    a = BankAccount("Ana", 100)
    a.deposit(10)
    a.withdraw(5)
    assert len(a) == 2
    assert a != BankAccount("Ana", 100)  # balance is 105 now


def test_no_fee_by_default():
    dan = BankAccount("dan", 500)
    dan.charge_fee()
    assert dan.balance == 500
    assert dan.transactions == []


def test_flat_fee():
    ana = BankAccount("Ana", 500, fee_strategy=FlatFee(3))
    ana.charge_fee()
    assert ana.balance == 497
    assert ana.transactions == ["fee 3"]


@pytest.mark.parametrize("balance, expected_fee", [
    (100, 5),
    (-100, 15),  # a negative balance
    (0, 5),  # the boundary: 0 is NOT below 0, so the normal fee applies
])
def test_fee_overdraft(balance, expected_fee):
    ana = BankAccount("Ana", balance, fee_strategy=OverdraftFee())
    ana.charge_fee()
    assert ana.balance == balance - expected_fee


def test_strategy_can_be_swapped_at_runtime():
    dan = BankAccount("Dan", 500)
    dan.fee_strategy = FlatFee(10)
    dan.charge_fee()
    assert dan.transactions == ["fee 10"]
    assert dan.balance == 490


def test_fee_strategy_cannot_be_instantiated():
    with pytest.raises(TypeError, match="abstract class FeeStrategy"):
        # pyrefly: ignore[bad-instantiation]
        FeeStrategy()  # ty: ignore[abstract-class-instantiation]


@pytest.mark.parametrize("strategy, balance, expected", [
    (FlatRate(0.05), -50, 0),
    (FlatRate(0.05), 0, 0),
    (TieredRate(), -50, 0),
    (TieredRate(), 500, 10.0),      # under 1000: only the 2% part
    (TieredRate(), 1500, 40.0),     # 1000 at 2% + 500 at 4%
])
def test_interest_strategy_calculate(strategy, balance, expected):
    assert strategy.calculate(balance) == expected


def test_month_end_uses_both_strategies():
    ion = BankAccount("Ion", 1000,
                      interest_strategy=FlatRate(0.05),
                      fee_strategy=FlatFee(3))
    ion.month_end()
    assert ion.balance == 1047.0            # 1000 + (1000 × 0.05) − 3
    assert ion.transactions ==  ["interest 50.0", "fee 3"]    # order matters


def test_interest_strategy_can_be_swapped_at_runtime():
    dan = BankAccount("Dan", 500)            # starts with NoInterest
    dan.interest_strategy = FlatRate(0.10)             # switch to 10% interest
    dan.apply_interest()
    assert dan.balance == 550.0               # 500 + (500 × 0.10)
    assert dan.transactions == ["interest 50.0"]

def test_large_withdrawal_triggers_alert():
    alert = LargeWithdrawalAlert(threshold=5_000)
    ana = BankAccount("Ana", 20_000)
    ana.subscribe(alert)
    ana.withdraw(6_000)
    assert alert.alerts == ["Ana withdrew 6000"]

def test_rejected_withdrawal_notification():
    log = AuditLog()
    ana = BankAccount("Ana", 100)
    ana.subscribe(log)
    with pytest.raises(ValueError):
        ana.withdraw(500)
    assert log.entries == []

def test_overdraft_notified_once_with_final_balance():
    log = AuditLog()
    ion = CheckingAccount("Ion", 50)
    ion.subscribe(log)
    ion.withdraw(100, 100)
    assert log.entries == [
        "Event: withdraw, Account: Ion, Amount: 100",
        "Event: withdraw, Account: Ion, Amount: 100",
        "Event: overdraft, Account: Ion, Amount: -150"
    ]

def test_small_withdrawal_no_alert():
    alert = LargeWithdrawalAlert(threshold=100)
    ana = BankAccount("Ana",500)
    ana.subscribe(alert)
    ana.withdraw(50)
    assert alert.alerts == []

def test_withdrawal_exactly_at_threshold():
    alert = LargeWithdrawalAlert(threshold=100)
    ana = BankAccount("Ana",500)
    ana.subscribe(alert)
    ana.withdraw(100)
    assert alert.alerts == []


def test_every_observer_is_notified():
    alert = LargeWithdrawalAlert(threshold=100)
    log = AuditLog()
    ana = CheckingAccount("Ana",100)
    ana.subscribe(alert)
    ana.subscribe(log)
    ana.withdraw(200)
    assert alert.alerts == ["Ana withdrew 200"]
    assert log.entries == [
        "Event: withdraw, Account: Ana, Amount: 200",
        "Event: overdraft, Account: Ana, Amount: -100"
        ]

def test_unsubscribed_observer_is_not_notified():
    alert = LargeWithdrawalAlert(threshold=100)
    ana = BankAccount("Ana", 300)
    ana.subscribe(alert)
    ana.unsubscribe(alert)
    ana.withdraw(200)
    assert alert.alerts == []

def test_observers_are_per_account():
    alert = LargeWithdrawalAlert(threshold=100)
    log = AuditLog()
    ana = CheckingAccount("Ana", 1_000)
    dan = CheckingAccount("Dan", 500)
    ana.subscribe(alert)
    ana.subscribe(log)
    ana.withdraw(1_100)
    dan.withdraw(600)
    assert alert.alerts == ["Ana withdrew 1100"]
    assert log.entries == [
        "Event: withdraw, Account: Ana, Amount: 1100",
        "Event: overdraft, Account: Ana, Amount: -100"
        ]

def test_unsubscribe_for_observer_without_subscribe():
    alert = LargeWithdrawalAlert(threshold=100)
    log = AuditLog()
    dan = CheckingAccount("Dan", 500)
    dan.subscribe(log)
    with pytest.raises(ValueError, match="Observer is not subscribed to this account" ):
        dan.unsubscribe(alert)
    assert dan._observers == [log]
