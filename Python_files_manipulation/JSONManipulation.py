import json


class JSONManipulation:

    def __init__(self, input_json_file):
        self.input_json = input_json_file

    def read_json_file(self):
        with open('{}'.format(self.input_json), 'r') as input_json:
            inp_data = str(input_json.read())
            json_data = json.loads(inp_data)
            print(json_data)

