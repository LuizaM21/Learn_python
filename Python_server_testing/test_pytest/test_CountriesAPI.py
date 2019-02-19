""" from cmd run command: pytest Python_server_testing/test_pytest -v
for a detailed run of the tests"""

from Python_server_testing.AllCountriesAPI import JsonAPI
from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation import FileHandling

country_config_csv = FileHandling.COUNTRY_CONFIG_CSV


def test_countries_details_type():
    response = JsonAPI().get_all_countries_details()
    assert isinstance(response, dict)


def test_countries_total_number():
    response = JsonAPI().get_countries_total_number()
    assert response == "Total [249] records found."


def test_country_iso_2_code():
    actual_iso_2_list = JsonAPI().get_all_country_iso_2_code()
    expected_iso_2_list = CSVManipulation(country_config_csv).read_csv_specific_column(1)
    print("actual_iso_2_list", sorted(actual_iso_2_list))
    print("expected_iso_2_list", sorted(expected_iso_2_list))

    if len(actual_iso_2_list) == len(expected_iso_2_list):
        check_list = zip(sorted(actual_iso_2_list), sorted(expected_iso_2_list))
        for actual, expected in check_list:
            print("actual", actual)
            print("expected", expected)
            assert actual == expected


if __name__ == '__main__':
    test_country_iso_2_code()
