import sys
import os
import pprint
import simplejson as json
import ConfigData as cd

config_data = cd.ConfigData.get_instance()
all_countries_json = config_data.get_value(cd.ALL_COUNTRIES_JSON)
quiz_json_file = config_data.get_value(cd.QUIZ_JSON)

COUNTRY_DETAILS = [
    ("Nepal", "Kathmandu",
     ("Kathmandu", "Patan", "Butwal"), "RUP",
     {"North": "China",
      "South": "India",
      "East": "India",
      "West": "China"}),

    ("China", "Beijing",
     ("Beijing", "Shanghai", "Shenzehn", "Hong Kong"), "YEN",
     {"North": "Mongolia, Russia",
      "South": "India, Nepal, Bhutan, Myanmar, Laos, Vietnam",
      "East": "Taiwan, South Korea",
      "West": "Kazakhstan, Kyrgyzstan, Tajikistan India"}),

    ("United States", "Washington",
     ("New York", "	Los Angeles", "Chicago", "Houston"), "USD",
     {"North": "Canada",
      "South": "Mexico",
      "East": "Atlantic Ocean",
      "West": "Pacific Ocean"}),

    ("England", "London",
     ("London", "York", "Bristol", "NewCastle"), "GBP",
     {"North": "Scotland, North Sea",
      "South": "English Channel",
      "East": "North Sea",
      "West": "Wales"}),
]


class JSONManipulation(object):

    def __init__(self, json_file=""):
        self.input_file = json_file

    @staticmethod
    def create_countries_json(country_name, capital, towns, currency, country_neighbours={}):
        country = {}
        country.setdefault("Country_name", country_name)
        country.setdefault("Capital", capital)
        country.setdefault("Towns", list(towns))
        country.setdefault("Currency", currency)
        country.setdefault("Country neighbours", country_neighbours)
        return country

    def read_json_file(self):
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                print("Read JSON from path: {}".format(self.input_file))
                with open(str(self.input_file), 'r', encoding="utf-8") as input_json:
                    inp_data = input_json.read()
                    inp_data = json.loads(inp_data)
                    return inp_data
            except Exception as e:
                print(e)
                return ""
        else:
            print("File not found under: {}".format(self.input_file))
            return ""

    @staticmethod
    def pretty_print_json_data(input_file, sort=True, indents=4):
        if type(input_file) is str:
            print(json.dumps(json.loads(input_file), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(input_file, sort_keys=sort, indent=indents))
            return None


if __name__ == "__main__":

    # country_json = [JSONManipulation.create_countries_json(*x) for x in COUNTRY_DETAILS]
    # pprint.pprint(country_json)
    # sys.exit()

    json_obj = JSONManipulation(all_countries_json)
    countries_json = json_obj.read_json_file()
    print(countries_json)
    # extract total number of countries from the json
    total_records_message = countries_json['RestResponse']['messages']
    print(total_records_message)

    country_results = countries_json['RestResponse']['result']
    # get country_code for a specific country represented by index in a list
    country_ISO2_code = country_results[2]['alpha2_code']
    print(country_ISO2_code)
    print(total_records_message)
    print(country_results)
    # [print(country['name']) for country in country_results]
    # [print(country['alpha3_code']) for country in country_results]
    # [print(country['alpha2_code']) for country in country_results]

    # apply custom pretty print function to display json in console
    # JSONManipulation.pretty_print_json_data(countries_json)
    pprint.pprint(countries_json)

    # print('\nDisplay {} file '.format(quiz_json_file))
    # quiz_json_obj = JSONManipulation(quiz_json_file).read_json_file()
    # print(quiz_json_obj)
    # JSONManipulation.pretty_print_json_data(quiz_json_obj)
    sys.exit()
