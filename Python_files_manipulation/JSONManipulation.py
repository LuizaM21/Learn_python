
import sys
import pprint
import simplejson as json
from pathlib import Path


global_folder_path = Path(r'E:\01_home_Learning_python\Python_project_files\Input_files\JSON_files')
all_countries_json = 'GetAllCountries.json'
quiz_json_file = 'quiz.json'


class JSONManipulation(object):

    def __init__(self, json_file):
        self.input_file = global_folder_path / json_file

    @staticmethod
    def create_countries_json(country_name, *towns, currency=None, country={}, **country_neighbours):
        country.setdefault(country_name, {})
        return country

    def read_json_file(self):
        if self.input_file.exists():
            print("Read JSON from path: {}".format(self.input_file.absolute()))
            with open(str(self.input_file), 'r', encoding="utf-8") as input_json:
                inp_data = input_json.read()
                inp_data = json.loads(inp_data)
                return inp_data
        else:
            print("File not found on path: {}".format(self))

    @staticmethod
    def pretty_print_json_data(input_file, sort=True, indents=4):
        if type(input_file) is str:
            print(json.dumps(json.loads(input_file), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(input_file, sort_keys=sort, indent=indents))
        return None


if __name__ == "__main__":
    country_list = ["Nepal", "China", "United States", "England"]
    for x in country_list:
        country_json = JSONManipulation.create_countries_json(x)
    country_json = [JSONManipulation.create_countries_json(x) for x in country_list]
    pprint.pprint(country_json)
    sys.exit()
    print('\nDisplay {} file '.format(all_countries_json))
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




