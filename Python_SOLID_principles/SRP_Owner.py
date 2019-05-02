

class Owner:
    """This class stores data about a phone owner"""

    def __init__(self, name='', age=None, gender='', phones_type=[], phone_subscriptions=[]):
        self.owner_name = name
        self.owner_age = age
        self.owner_gender = gender
        self.owner_details = [str(name), str(age), str(gender)]
        self.phones_type = phones_type
        self.phone_subscriptions = phone_subscriptions

    """---------------------------------------------------------------------"""
    def set_owner_details(self, name, age, gender):
        self.owner_name = str(name)
        self.owner_age = str(age)
        self.owner_gender = str(gender)

    """---------------------------------------------------------------------"""
    def get_owner_name(self):
        return self.owner_name

    def set_owner_name(self, input_name):
        self.owner_name = input_name
        return self.owner_name

    """---------------------------------------------------------------------"""
    def get_owner_age(self):
        return self.owner_age

    def set_owner_age(self, input_age):
        self.owner_age = input_age
        return self.owner_age

    """---------------------------------------------------------------------"""
    def get_owner_gender(self):
        return self.owner_gender

    def set_owner_gender(self, input_gender):
        self.owner_gender = input_gender
        return self.owner_gender

    """---------------------------------------------------------------------"""
    def get_owner_phone_devices(self):
        return self.phones_type

    def set_owner_phone_devices(self, device_list=[]):
        self.phones_type = device_list
        return self.phones_type
