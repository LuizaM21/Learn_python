"""Get all countries API that returns ISO2 and ISO3"""
import requests
import pprint
import simplejson as json

ALL_COUNTRIES_REQUEST = "http://services.groupkt.com/country/get/all"


def get_all_countries():
    """GEt the api response and evaluate the response as a valid JSON content"""
    api_response = requests.get(ALL_COUNTRIES_REQUEST).text
    json_response = json.loads(api_response)
    return json_response


def get_all_iso_2_code():
    pass


def get_all_iso_3_code():
    pass


if __name__ == '__main__':
    pprint.pprint(get_all_countries())

