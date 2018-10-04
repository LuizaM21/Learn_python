import simplejson as json
from pathlib import Path


class JSONManipulation:

    folder_path = Path('C:\Learning_Python_Scripts\Python_files_manipulation')
    file_to_open = folder_path / 'GetAllCountries.json'

    def read_json_file(self):
        if self.file_to_open.exists():
            print("Read JSON from path: {}".format(self.file_to_open))
            with open(self.file_to_open.name, 'r', encoding="utf-8") as input_json:
                inp_data = input_json.read()
                return inp_data
        else:
            print("File not found on path: {}".format(self.file_to_open))


if __name__ == "__main__":
    jsonM_obj = JSONManipulation()
    j_data = jsonM_obj.read_json_file()
    print(type(j_data))
    # utf-8-sig
    print(json.loads(j_data))
    print(type(json.loads(j_data)))
    print(jsonM_obj.file_to_open)



