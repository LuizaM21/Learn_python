from pprint import pprint
from Python_SOLID_principles.SRP_Owner import Owner
from Python_SOLID_principles.SRP_MobyleType import MobileType
from Python_SOLID_principles.SRP_Subscriptions import Subscriptions


class Customers:

    def __init__(self, owner, subscriptions, phone_type):
        self.owner = owner
        self.subscriptions = subscriptions
        self.phone_type = phone_type

    def get_customer_details(self):
        return [self.owner.owner_details, self.subscriptions, self.phone_type]

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
    owner_1 = Owner('john', 23, 'm')
    owner_2 = Owner("Jane", 25, 'f')

    mobile_lg = MobileType('LG', 2015, 'black')
    mobile_samsung = MobileType('Samsung', 2016, 'red')
    mobile_huawei = MobileType('Huawei', 2017, 'P20')
    mobile_nokia = MobileType('Nokia', 2018, 'Tempered Blue')

    subscription_1 = Subscriptions('0741111111', 'prepay')
    subscription_2 = Subscriptions('0752222222', 'prepay')
    subscription_3 = Subscriptions('0753333333', 'prepay')
    subscription_4 = Subscriptions('0744444444', 'prepay')
    customer_1 = Customers(owner_1,
                           [subscription_1.subscriptions_details, subscription_2.subscriptions_details],
                           [mobile_lg.mobile_details, mobile_samsung.mobile_details])

    customer_2 = Customers(owner_2,
                           [subscription_3.subscriptions_details, subscription_4.subscriptions_details],
                           [mobile_huawei.mobile_details, mobile_nokia.mobile_details])

    pprint(customer_1.get_customer_details())
    print()
    pprint(customer_2.get_customer_details())

