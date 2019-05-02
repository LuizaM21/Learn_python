

class Subscriptions:

    def __init__(self, phone_number='', subscription_type=''):
        self.phone_number = phone_number
        self.subscription_type = subscription_type
        self.subscriptions_details = [phone_number, subscription_type]

    def get_user_phone_number(self):
        return self.phone_number

    def get_user_subscription_type(self):
        return self.subscription_type

    def get_subscriptions_details(self):
        return self.subscriptions_details



