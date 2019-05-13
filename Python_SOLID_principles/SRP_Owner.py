"""
Liskov Substitution Principle:
Ability to replace any instance of a parent class with an instance of its child classes without negative effects.

Conditions:
- Any child method should return the same type as that of its parent
- Method signature must match (must take the same number of parameters)
- The preconditions for any method can’t be greater than that of its parent
- Post conditions must be at least equal to that of its parent
- Exception types must match
"""
from validate_email import validate_email


class Owner:
    """This class stores data about a phone owner"""

    def __init__(self, name='', age=None, gender=''):
        self.owner_name = name
        self.owner_age = age
        self.owner_gender = gender
        self.phones_type = []

    def __str__(self):
        return f'Name: {self.owner_name}, ' \
               f'Age: {self.owner_age}, ' \
               f'Gender: {self.owner_gender} '

    """---------------------------------------------------------------------"""
    def set_owner_details(self, name, age, gender):
        self.owner_name = name
        self.owner_age = age
        self.owner_gender = gender

    """---------------------------------------------------------------------"""
    def get_owner_name(self):
        return f'Owner name: {self.owner_name}'

    def set_owner_name(self, input_name):
        self.owner_name = input_name
        return self.owner_name

    """---------------------------------------------------------------------"""
    def get_owner_age(self):
        return f'Owner Age: {self.owner_age}'

    def set_owner_age(self, input_age):
        self.owner_age = input_age
        return self.owner_age

    """---------------------------------------------------------------------"""
    def get_owner_gender(self):
        return f'Owner gender: {self.owner_gender}'

    def set_owner_gender(self, input_gender):
        self.owner_gender = input_gender
        return self.owner_gender

    """---------------------------------------------------------------------"""
    def get_owner_phone_devices(self):
        return f'Phone type: {self.phones_type}'

    def set_owner_phone_devices(self, device_list=[]):
        self.phones_type = device_list
        return self.phones_type


class PremiumCustomer(Owner):
    """Respects the OCP (Open-Close principle)"""

    RANK_4 = 'Bronze'
    RANK_3 = 'Silver'
    RANK_2 = 'Gold'
    RANK_1 = 'Platinum'

    def __init__(self, name, age, gender, rank):
        super().__init__(name, age, gender)
        self.owner_rank = rank

    def __str__(self):
        return f'Name: {self.owner_name}, ' \
               f'Age: {self.owner_age}, ' \
               f'Gender: {self.owner_gender} ' \
               f'Rank: {self.owner_rank} client'

    def set_customer_rank(self, rank):
        self.owner_rank = rank


class ValidCustomer:
    def __init__(self, owner,  email):
        self.owner = owner
        self.owner_email = email

    def check_age(self):
        if self.owner.owner_age < 18:
            return False
        return True

    def validate_customer_email(self):
        is_valid = validate_email(self.owner_email)
        if is_valid:
            return True
        return False


if __name__ == '__main__':

    owner_1 = PremiumCustomer("Melisande", 15, 'f', PremiumCustomer.RANK_4)
    print(owner_1)
    print(owner_1.get_owner_name())
    print(owner_1.get_owner_age(), '\n')

    owner_1.set_owner_details("Gamora", 13, 'f')
    owner_1.set_customer_rank(PremiumCustomer.RANK_1)
    print(owner_1)
    print(owner_1.get_owner_name())
    print(owner_1.get_owner_age())
    valid_user = ValidCustomer(owner_1, 'test.test@test.com')
    print(valid_user.validate_customer_email())
    print(valid_user.check_age())
