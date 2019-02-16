"""Get all countries API that returns ISO2 and ISO3"""
import requests
import pprint
import simplejson as json


class JsonAPI:
    def __init__(self, iso_code=None):
        self.api_request = "http://services.groupkt.com/"
        self.iso__code_2 = iso_code

    @staticmethod
    def get_all_countries_details():
        """Get the API response and evaluate the response as a valid JSON content"""
        api_response = requests.get("http://services.groupkt.com/country/get/all").text
        all_countries_response = json.loads(api_response)
        return all_countries_response

    # http://services.groupkt.com/state/get/{countryCode}/all
    def get_country_details(self):
        country_details_response = requests.get(self.api_request + "state/get/" + self.iso__code_2 + "/all").text
        country_details = json.loads(country_details_response)
        return country_details

    def get_all_country_iso_2_code(self):
        pass

    def get_all_country_iso_3_code(self):
        pass


if __name__ == '__main__':
    # pprint.pprint(JsonAPI.get_all_countries_details())
    pprint.pprint(JsonAPI("IND").get_country_details())

