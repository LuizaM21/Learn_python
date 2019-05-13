"""
SRP - Single Responsibility Principle
Every module, class, or function should have responsibility over a single part of the functionality provided
by the software, and that responsibility should be entirely encapsulated by the class

Conditions:
- A class or module should have one, and only one, reason to be changed.
- Too much responsibility leads to coupling between classes or modules.
- Isolate change by looking closely at the things that make the whole and separate them logically.
"""


class Subscriptions:

    def __init__(self, phone_number='', subscription_type=''):
        self.phone_number = phone_number
        self.subscription_type = subscription_type

    def __str__(self):
        return f'Phone Number: {self.phone_number}' \
               f'Subscription Type: {self.subscription_type}'

    def get_user_phone_number(self):
        return self.phone_number

    def get_user_subscription_type(self):
        return self.subscription_type

