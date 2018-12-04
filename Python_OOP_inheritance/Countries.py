
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


class CityDetails:
    def __init__(self, city_name, city_location, capital=False):
        self.city_name = city_name
        self.city_location = city_location
        self.is_capital = capital

    def get_city_details(self):
        city_details = "Situated in {0} of the country \nCity capital of the country = {1}"\
                        .format(self.city_location, str(self.is_capital))
        return city_details


class EnglandCountry(Countries):
    """Represent all the particularities that this country has"""

    def __init__(self, capital_city, residents_number, mountains=False, sea=False, ocean=False, islands_num=3):
        """initialize attributes for England country"""
        self.has_ocean = ocean
        self.number_of_isles = islands_num

        # bounds the parent class init method with the inherited class init method
        super().__init__(capital_city, residents_number, mountains, sea)
        self.city_details = CityDetails(capital_city, "North-East", True)

    def get_england_extra_details(self):
        england_details = "Country has ocean opening: {0}\n" \
                          "Country number of isles: {1}".format(str(self.has_ocean), str(self.number_of_isles))
        return england_details


if __name__ == '__main__':
    england_country = EnglandCountry('London', 100000, False, True, True, 4)
    print(england_country.get_all_country_details())
    print(england_country.get_england_extra_details())
    print(england_country.city_details.get_city_details())

