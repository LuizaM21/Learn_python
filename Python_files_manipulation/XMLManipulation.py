import os
import xml.dom.minidom as minidom
import sys
import ConfigData as cd

config_data = cd.ConfigData.get_instance()
input_xml_file = config_data.get_value(cd.BREAKFAST_MENU_XML)
output_file = config_data.get_value(cd.OUTPUT_XML_FILE)


class XMLManipulation(object):
    # configData = cf.ConfigData.get_instance()
    # TODO: Config paths from Config file
    # BASE_DIR = configData.get_value(cf.CONFIG_INPUT_LIST[2])

    def __init__(self, input_file):
        self.input_file = input_file

    def read_xml_file(self):
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                str_xml = ""
                with open(str(self.input_file), 'r', encoding='utf-8') as input_data:
                    print("Read from path: {}".format(self.input_file))
                    file_content = input_data.read().splitlines()
                    input_data.close()
                if type(file_content) == list:
                    str_xml = "".join(file_content)
                return str_xml
            except Exception as e:
                return str(e)
        else:
            return FileNotFoundError

    @staticmethod
    def pretty_print_xml_data(input_file):
        xml_str = minidom.parseString(input_file).toprettyxml()
        # remove empty lines returned from minidom parser
        correct_format = "".join([s for s in xml_str.strip().splitlines(True) if s.strip()])
        return correct_format


if __name__ == "__main__":
    xml_data = XMLManipulation(input_xml_file).read_xml_file()
    with open(str(output_file), 'w') as output_f:
        print("write file in: {}".format(output_file))
        output_f.write(xml_data)
    print(XMLManipulation.pretty_print_xml_data(xml_data))
    sys.exit()

