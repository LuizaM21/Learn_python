

class Countries:

    def __init__(self, capital_city, residents_number, mountains=False, sea=False):
        self.capital = capital_city
        self.resident_num = residents_number
        self.has_mountains = mountains
        self.has_sea = sea

    def set_capital_city(self, capital_country):
        """Set the city capital of a country"""
        self.capital = capital_country

    def get_capital_city(self):
        """Return the city capital of a country"""
        return self.capital.title()

    def set_country_resident_number(self, residents_num):
        """Set the total number of residents of a country"""
        self.resident_num = residents_num

    def set_country_demographics(self, has_mountains, has_sea):
        """Set the value to True if the country has mountains and sea"""
        self.has_mountains = has_mountains
        self.has_sea = has_sea

class Country(Countries):
    """Represent all the particularities that a class has"""


if __name__ == '__main__':
    pass
