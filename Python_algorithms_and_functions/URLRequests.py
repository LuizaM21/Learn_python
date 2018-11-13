#!/usr/bin/env python

"""
Modificati 02-requests_full.py sa afiseze pentru fiecare resident titlul filmelor in care a aparut (pot fi ordonate).

Aveti grija, daca faceti asta pentru toate planetele o sa dureze, puteti limita scriptul sa ruleze doar pentru cateva planete.
"""

import json
import sys

import requests
import pprint

BASE_URL = "https://swapi.co/"


def get_data_for_num_of_planets(planet_num):
    """Return data for the first three planets."""

    url_to_call = requests.compat.urljoin(BASE_URL, "/api/planets")
    full_data = []
    for i in range(0, planet_num):
        print("Calling page: ", url_to_call)
        planets_result_raw = requests.get(url_to_call)

        if not planets_result_raw.ok:
            print("Current status code: ", planets_result_raw.status_code)
            sys.exit(1)

        planets_json = json.loads(planets_result_raw.text)
        full_data.extend(planets_json['results'])

        next_page = planets_json.get('next', i)
        if next_page is None:
            break
        url_to_call = next_page
    return full_data


def get_name(url):
    """Get resident name from `url`."""
    print("Calling page: ", url)
    data = requests.get(url)
    if not data.ok:
        print("Am primit status code ", data.status_code)
        sys.exit(2)

    resident = json.loads(data.text)
    return resident['name']


def get_planet_name_and_residents_num(planet_data):
    planets_and_residents = []
    for index, planet in enumerate(planet_data, start=1):
        pprint.pprint(planet)
        name = planet['name']
        residents_count = len(planet['residents'])
        planets_and_residents.append(("Planet number: " + str(index),
                                      "Planet name: " + str(name),
                                      "Number of residents: " + str(residents_count)))
    return planets_and_residents


def get_residents_films(planet_data):
    resident_list = [("Resident number: " + str(index), x['residents']) for index, x in enumerate(planet_data, start=1)]
    resident_movies = []
    for resident, rez_request in resident_list:
        for movie_req in rez_request:
            data = requests.get(movie_req)
            response = json.dumps(data.text)
            resident_film = response['films']
            resident_movies.append(resident_film)
    return resident_movies

# residents_names = []
# for url in planet['residents']:
#     residents_names.append(get_name(url))
#
#     planets_and_residents.append((name, residents_count, residents_names))
#
# planets_and_residents.sort(key=lambda x: x[1], reverse=True)
#
# for name, residents_count, residents in planets_and_residents:
#     print("{:15} -> {}".format(name, residents_count))
#
#     for name_r in residents:
#         print("\t - ", name_r)
#
# print("\n\n\nPlanets with more then on resident\n")
#
# # more_then_1 = filter(lambda x: x[1] > 1, planets_and_residents)
# more_then_1 = [x for x in planets_and_residents if x[1] > 1]
# for name, residents_count, residents in more_then_1:
#     print("{:15} -> {}".format(name, residents_count))
#
#     for name_r in residents:
#         print("\t - ", name_r)


if __name__ == "__main__":
    """Returns a list of tuples with the name of planets and the corresponding residents"""
    planets_data = get_data_for_num_of_planets(1)
    # pprint.pprint(planets_data)
    pprint.pprint(get_residents_films(planets_data))
    # pprint.pprint(get_planet_name_and_residence_num(planets_data))
