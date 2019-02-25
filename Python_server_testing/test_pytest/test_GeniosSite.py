""" from cmd run command:
pytest Python_server_testing/test_pytest/test_GeniosSite.py -v
for a detailed run of the tests only for this test file"""

import pprint
import ConfigData as config_data
from Python_server_testing.GeniosSite import GeniosServer
from Python_files_manipulation.CSVManipulation import CSVManipulation as csv_manipulation

c_data = config_data.ConfigData.get_instance()
BASE_URL = "https://www.genios.ro/"
site = GeniosServer(BASE_URL)
SITE_LIST = c_data.get_value(config_data.SITE_LIST_CSV)
CUBE_TYPES = c_data.get_value(config_data.CUBE_TYPES_CSV)


def test_response_content_type():
    headers = site.get_response_headers()
    content_type = headers["Content-Type"]
    assert content_type == "text/html; charset=UTF-8"


def test_site_connection_type():
    headers = site.get_response_headers()
    connection_type = headers["Connection"]
    assert connection_type == "Upgrade, Keep-Alive"


def test_site_link_lists():
    actual_links = site.get_site_link_lists()
    expected_links = csv_manipulation(SITE_LIST).read_csv_lines()

    if len(actual_links) == len(expected_links):
        check_link_list = zip(sorted(actual_links), sorted(expected_links))
        for actual, expected in check_link_list:
            assert actual == expected
    else:
        assert False


def test_all_cubes_types():
    cube_name = csv_manipulation(CUBE_TYPES).read_csv_specific_column(0)
    cube_link = csv_manipulation(CUBE_TYPES).read_csv_specific_column(1)
    expected_cube_types = dict(zip(cube_name, cube_link))
    actual_cube_types = site.get_all_cubes_types()

    if len(actual_cube_types) == len(expected_cube_types):
        for key in actual_cube_types.keys():
            assert actual_cube_types[key] == expected_cube_types[key]
    else:
        assert False


if __name__ == '__main__':
    # test_response_content_type()
    # test_site_connection_type()
    # test_site_link_lists()
    test_all_cubes_types()

