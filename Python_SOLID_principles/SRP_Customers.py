from pprint import pprint
from Python_SOLID_principles.SRP_Owner import Owner, PremiumCustomer
from Python_SOLID_principles.SRP_MobyleType import MobileType
from Python_SOLID_principles.SRP_Subscriptions import Subscriptions
from typing import List


class Customers:

    def __init__(self, owner, subscriptions: List[Subscriptions], phone_type: List[MobileType]):
        self.owner = owner
        self.subscriptions = subscriptions
        self.phone_type = phone_type

    def __str__(self):
        subs = ''.join([str(x) for x in self.subscriptions])
        pt = ''.join([str(x) for x in self.phone_type])

        return {'Owner': str(self.owner),
                'Subscriptions': subs,
                'Phone Type': pt}

    def get_user_phone_numbers(self):
        pass

    def get_user_total_num_of_subscription(self):
        pass

    def get_user_phone_types(self):
        pass

    def create_user_phone_type(self):
        pass

    def create_user_subscription_type(self):
        pass

    def update_subscription_type(self):
        pass


if __name__ == '__main__':
    mobile_lg = MobileType('LG', 2015, 'black')
    mobile_samsung = MobileType('Samsung', 2016, 'red')
    mobile_huawei = MobileType('Huawei', 2017, 'P20')
    mobile_nokia = MobileType('Nokia', 2018, 'Tempered Blue')

    subscription_1 = Subscriptions('0741111111', 'prepay')
    subscription_2 = Subscriptions('0752222222', 'prepay')
    subscription_3 = Subscriptions('0753333333', 'prepay')
    subscription_4 = Subscriptions('0744444444', 'prepay')

    owner_1 = Owner('john', 23, 'm')
    owner_2 = Owner("Jane", 25, 'f')
    customer_rank = PremiumCustomer('john', 23, 'm', PremiumCustomer.RANK_1)
    print(customer_rank.get_owner_age())

    customer_1 = Customers(owner_1, [subscription_1, subscription_2], [mobile_lg, mobile_samsung])
    customer_2 = Customers(owner_2, [subscription_3, subscription_4], [mobile_huawei, mobile_nokia])

    pprint(customer_1.__str__())
    print()
    pprint(customer_2.__str__())
    print(customer_rank)

