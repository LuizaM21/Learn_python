import xml.dom.minidom as minidom
import xml.etree.cElementTree as ET
import sys
import ConfigData as cf
from pathlib import Path

BASE_DIR = Path(r"C:\Learning_Python_Scripts\Python_project_files\Input_files\XML_files")
xml_file = "Cell3DReport.xml"


class XMLManipulation(object):
    # configData = cf.ConfigData.get_instance()
    # TODO: Config paths from Config file
    # BASE_DIR = configData.get_value(cf.CONFIG_INPUT_LIST[2])

    def __init__(self, xml_f):
        self.input_file = BASE_DIR / xml_f

    def read_xml_file(self):
        if self.input_file.exists():
            print(type(self.input_file))
            with open(str(self.input_file), 'r', encoding='utf-8') as input_data:
                print("Read from path: {}".format(self.input_file))
                file_content = input_data.read().splitlines()
                input_data.close()
                if type(file_content) == list:
                    str_xml = "".join(file_content)
                return str_xml
        else:
            return FileNotFoundError

    @staticmethod
    def pretty_print_xml_data(input_file, sort=True, indents=4):
        # TODO: refactor the pretty_print to work for xml files
        if type(input_file) is str:
            print(json.dumps(json.loads(input_file), sort_keys=sort, indent=indents))
        else:
            print(json.dumps(input_file, sort_keys=sort, indent=indents))
        return None


if __name__ == "__main__":
    print(type(XMLManipulation(xml_file).read_xml_file()))
    print(XMLManipulation(xml_file).read_xml_file())
    sys.exit()

