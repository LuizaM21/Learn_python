

class Subscriptions:

    def __init__(self, phone_number='', subscription_type=''):
        self.phone_number = phone_number
        self.subscription_type = subscription_type

    def __str__(self):
        return f'Phone Number: {self.phone_number} ' \
               f'Subscription Type: {self.subscription_type}'

    def get_user_phone_number(self):
        return self.phone_number

    def get_user_subscription_type(self):
        return self.subscription_type

