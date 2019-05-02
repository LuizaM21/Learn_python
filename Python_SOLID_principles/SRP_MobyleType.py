
class MobileType:
    """This class stores details about a phone model"""

    def __init__(self, model_name='', fabrication_year='', color=''):
        self.model_name = str(model_name)
        self.fabrication_year = str(fabrication_year)
        self.color = str(color)
        self.mobile_details = [self.model_name, self.fabrication_year, self.color]

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
        return self.mobile_details


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
