""" from cmd run command: pytest Python_server_testing/test_pytest -v
for a detailed run of the tests"""

from Python_server_testing.AllCountriesAPI import JsonAPI


def test_countries_details_resp_time():
    response_time = JsonAPI().get_all_countries_details()[1]
    assert response_time <= 1


def test_countries_total_number():
    response = JsonAPI().get_countries_total_number()
    assert response == "Total [249] records found."


def test_country_iso_2_code():
    iso_2_list = JsonAPI().get_all_country_iso_2_code()
    print(iso_2_list)
    assert len(iso_2_list) == 249

