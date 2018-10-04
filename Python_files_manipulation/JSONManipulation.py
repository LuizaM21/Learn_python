import simplejson as json
from pathlib import Path


global_folder_path = Path('C:\Learning_Python_Scripts\Python_files_manipulation')
get_all_countries_file = 'GetAllCountries.json'
quiz_json_file = 'quiz.json'


class JSONManipulation:

    def __init__(self, json_file):
        self.input_file = global_folder_path / json_file

    def read_json_file(self):
        if self.input_file.exists():
            print("Read JSON from path: {}".format(self.input_file))
            with open(self.input_file.name, 'r', encoding="utf-8") as input_json:
                inp_data = input_json.read()
                self._pretty_print_json_data(inp_data)
                return inp_data
        else:
            print("File not found on path: {}".format(self.input_file))

    @staticmethod
    def _pretty_print_json_data(input_file, sort=True, indents=4):
        if type(input_file) is str:
            print(json.dumps(json.loads(input_file), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(input_file, sort_keys=sort, indent=indents))
        return None


if __name__ == "__main__":
    print('\nDisplay {} file '.format(get_all_countries_file))
    countries_json_obj = JSONManipulation(get_all_countries_file).read_json_file()
    print('\nDisplay {} file '.format(quiz_json_file))
    quiz_json_obj = JSONManipulation(quiz_json_file).read_json_file()




