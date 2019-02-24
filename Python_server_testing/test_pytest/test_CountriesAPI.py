""" from cmd run command:
pytest Python_server_testing/test_pytest/test_CountriesAPI.py -v
for a detailed run of the tests"""

from Python_server_testing.AllCountriesAPI import JsonAPI
from Python_files_manipulation.CSVManipulation import CSVManipulation as csv_manipulation
import ConfigData as config_data

c_data = config_data.ConfigData.get_instance()
country_config_csv = c_data.get_value(config_data.COUNTRY_CONFIG_CSV)


def test_countries_details_type():
    response = JsonAPI().get_all_countries_details()
    assert isinstance(response, dict)


def test_countries_total_number():
    response = JsonAPI().get_countries_total_number()
    assert response == "Total [249] records found."


def test_country_iso_2_code():
    actual_iso_2_list = JsonAPI().get_all_country_iso_2_code()
    expected_iso_2_list = csv_manipulation(country_config_csv).read_csv_specific_column(1)

    if len(actual_iso_2_list) == len(expected_iso_2_list):
        check_list = zip(sorted(actual_iso_2_list), sorted(expected_iso_2_list))
        for actual, expected in check_list:
            assert actual == expected
    else:
        assert False


if __name__ == '__main__':
    test_country_iso_2_code()
