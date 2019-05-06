

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
               f'Gender: {self.owner_gender},'

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
