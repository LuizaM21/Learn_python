
class Countries(object):

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

    def get_all_country_details(self):
        """Return all the common details of a country"""
        country_details = "Country capital: {0} " \
                          "\nCountry residence number: {1} " \
                          "\nCountry has mountains: {2} " \
                          "\nCountry has sea: {3}".format(self.capital, str(self.resident_num), str(self.has_mountains), str(self.has_sea))
        return country_details


class EnglandCountry(Countries):
    """Represent all the particularities that this country has"""

    def __init__(self, capital_city, residents_number, mountains=False, sea=False, ocean=True, islands_num=3):
        """initialize attributes for England country"""
        self.has_ocean = ocean
        self.number_of_isles = islands_num
        # bounds the parent class init method with the inherited class init method
        super().__init__(capital_city, residents_number, mountains, sea)

    def get_england_extra_details(self):
        england_details = "Country has ocean opening: {0}\n" \
                          "Country number of isles: {1}".format(self.has_ocean, self.number_of_isles)
        return england_details


if __name__ == '__main__':
    england_country = EnglandCountry('London', 100000, False, True, False, 4)
    print(england_country.get_all_country_details())
    print(england_country.get_england_extra_details())
