"""Scope of the project is to collect JSON response from different API calls,
verify data correctness using pytest module,
output the test suite status and log the project activity into a text file"""

from requests import request


def get_weather_details():
    weather_url = "https://climacell-microweather-v1.p.rapidapi.com/weather/nowcast"

    url_headers = {
        'x-rapidapi-host': "climacell-microweather-v1.p.rapidapi.com",
        'x-rapidapi-key': "f32c83520emsh7b23dbf5988f5dap1e3d73jsn8369312be7d1"
    }

    querystring = {"fields": "precipitation",
                   "unit_system": "si",
                   "lat": "42.8237618",
                   "lon": "-71.2216286"}
    api_response = request("GET", weather_url, headers=url_headers, params=querystring)
    return api_response.text


def get_geo_db_response():
    url = "https://wft-geo-db.p.rapidapi.com/v1/locale/locales"

    headers = {
        'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
        'x-rapidapi-key': "f32c83520emsh7b23dbf5988f5dap1e3d73jsn8369312be7d1"
        }
    response = request("GET", url, headers=headers)
    return response.text


if __name__ == '__main__':
    print("-----------weather details--------------")
    print(get_weather_details())

    print("\n-----------geo_db details--------------")
    print(get_geo_db_response())


