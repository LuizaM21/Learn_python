"""Get all countries API that returns ISO2 and ISO3"""
import requests
import pprint
import simplejson as json
from Python_server_testing.Decorators import request_duration


class JsonAPI:
    def __init__(self, iso_code=None):
        self.api_request = "http://services.groupkt.com/"
        self.iso__code_2 = iso_code

    def get_all_countries_details(self):
        """Get the API response and evaluate the response as a valid JSON content
        :return all_countries_response"""
        api_response = requests.get(self.api_request + "country/get/all")
        if api_response.ok:
            try:
                all_countries_response = json.loads(api_response.text)
                return all_countries_response
            except Exception as e:
                print(e)
                return
        else:
            print("Bad request!")

    # Request example: http://services.groupkt.com/state/get/{countryCode}/all
    @request_duration
    def get_specific_country_details(self):
        """:return country_details in json format"""
        country_details_response = requests.get(self.api_request + "state/get/" + self.iso__code_2 + "/all")
        if country_details_response.ok:
            try:
                country_details = json.loads(country_details_response.text)
                return country_details
            except Exception as e:
                print(e)
                return False
        else:
            print("Bad Request!")

    @request_duration
    def get_countries_total_number(self):
        """:return total_number of the countries in the existent json response"""
        if self.get_all_countries_details():
            try:
                countries_json = self.get_all_countries_details()
                total_number = countries_json['RestResponse']['messages'][0]
                return total_number
            except Exception as e:
                print(e)
                return
        else:
            print("Not a valid JSON response!")

    @request_duration
    def get_all_country_iso_2_code(self):
        """:return ISO 2 country code in a list"""
        if self.get_all_countries_details():
            try:
                countries_json = self.get_all_countries_details()
                total_records_message = countries_json['RestResponse']['messages'][0]
                print("total_records_message: ", total_records_message)

                iso_2_code_list = countries_json['RestResponse']['result']
                iso_2_code_list = [x['alpha2_code'] for x in iso_2_code_list]
                return iso_2_code_list
            except Exception as e:
                print(e)
                return
        else:
            print("Not a valid JSON response!")

    @request_duration
    def get_all_country_iso_3_code(self):
        """:return ISO 3 country code in a list"""
        if self.get_all_countries_details():
            try:
                # extract json part without duration by accessing only the first element of the tuple
                countries_json = self.get_all_countries_details()
                iso_3_code_list = countries_json['RestResponse']['result']
                iso_3_code_list = [x['alpha3_code'] for x in iso_3_code_list]
                return iso_3_code_list
            except Exception as e:
                print(e)
                return
        else:
            print("Not a valid JSON response!")


if __name__ == '__main__':
    pprint.pprint(JsonAPI().get_all_countries_details())
    # pprint.pprint(JsonAPI("IND").get_specific_country_details())
    # print(JsonAPI().get_all_country_iso_2_code())
    print(JsonAPI().get_all_country_iso_3_code())
    # print(JsonAPI().get_countries_total_number())

