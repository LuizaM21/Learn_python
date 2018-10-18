import xml.dom.minidom as minidom
import sys
import ConfigData as cf
from pathlib import Path

BASE_DIR = Path(r"C:\Learning_Python_Scripts\Python_project_files\Input_files\XML_files")
OUTPUT_DIR = Path(r"C:\Learning_Python_Scripts\Python_project_files\Output_files\XML_files")
xml_file = "Cell3DReport.xml"
output_file = OUTPUT_DIR / "output_xml_file.xml"


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
    def pretty_print_xml_data(input_file):
        xml_str = minidom.parseString(input_file).toprettyxml()
        # remove empty lines returned from minidom parser
        correct_format = "".join([s for s in xml_str.strip().splitlines(True) if s.strip()])
        return correct_format


if __name__ == "__main__":
    xml_data = XMLManipulation(xml_file).read_xml_file()
    with open(str(output_file), 'w') as output_f:
        print("write file in: {}".format(output_file))
        output_f.write(xml_data)
    print(XMLManipulation.pretty_print_xml_data(xml_data))
    sys.exit()

