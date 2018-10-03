import json
from pathlib import Path


class JSONManipulation:

    folder_path = Path('C:\Learning_Python_Scripts\Python_files_manipulation')
    file_to_open = folder_path / 'GetAllCountries.json'

    def read_json_file(self):
        if self.file_to_open.exists():
            print("Read JSON from path: {}".format(self.file_to_open))
            with open(self.file_to_open.name, 'r', encoding="UTF-8") as input_json:
                # inp_data = input_json.read()
                j_data = json.loads(input_json)
                return j_data
        else:
            print("File not found on path: {}".format(self.file_to_open))


if __name__ == "__main__":
    jsonM_obj = JSONManipulation()
    print(jsonM_obj.read_json_file())
    print(jsonM_obj.file_to_open)



