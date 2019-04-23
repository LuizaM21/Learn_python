
class MobileType:
    """This class stores details about a phone model"""

    def __init__(self, model_name, fabrication_year, color):
        self.model_name = str(model_name)
        self.fabrication_year = str(fabrication_year)
        self.color = str(color)

    def get_mobile_name(self):
        return self.model_name

    def get_mobile_fabrication_year(self):
        return self.fabrication_year

    def get_model_color(self):
        return self.color

    def set_mobile_name(self, input_name):
        self.model_name = input_name
        return self.model_name

    def set_mobile_fabrication_year(self, input_year):
        self.fabrication_year = input_year
        return self.fabrication_year

    def set_mobile_color(self, input_color):
        self.color = input_color
        return self.color

    def get_mobile_details(self):
        all_details = [self.model_name, self.fabrication_year, self.color]
        print("Phone model name: {0}"
              "Phone year of fabrication: {1}"
              "Phone color: {2}".format(all_details[0], all_details[1], all_details[2]))
        return all_details


class Owner:
    """This class stores data about a phone owner"""
    def __init__(self, name, age, gender):
        self.owner_name = str(name)
        self.owner_age = str(age)
        self.owner_gender = str(gender)
        self.user_id = ''
        self.phones_type = []
        self.phone_subscriptions = []

    def get_owner_name(self):
        return self.owner_name

    def get_owner_age(self):
        return self.owner_age

    def get_owner_gender(self):
        return self.owner_gender

    def get_owner_phone_devices(self):
        return self.phones_type

    def set_owner_name(self, input_name):
        self.owner_name = input_name
        return self.owner_name

    def set_owner_age(self, input_age):
        self.owner_age = input_age
        return self.owner_age

    def set_owner_gender(self, input_gender):
        self.owner_gender = input_gender
        return self.owner_gender

    def set_owner_phone_devices(self, device_list=[]):
        self.phones_type = device_list
        return self.phones_type

    def create_user_phone_type(self):
        pass


class Abonament:

    def __init__(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id


if __name__ == '__main__':
    huawei = MobileType('P20', 2017, 'black')
    print('phone name = ', huawei.get_mobile_name())
    print('fabrication year = ', huawei.get_mobile_fabrication_year())
    print('phone color = ', huawei.get_model_color())

    huawei.set_mobile_name('P20-Lite')
    huawei.set_mobile_fabrication_year(2018)
    huawei.set_mobile_color('white')

    print('phone name = ', huawei.get_mobile_name())
    print('fabrication year = ', huawei.get_mobile_fabrication_year())
    print('phone color = ', huawei.get_model_color())
