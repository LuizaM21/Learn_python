#!/usr/bin/env python

"""
Modificati 02-requests_full.py sa afiseze pentru fiecare resident titlul filmelor in care a aparut (pot fi ordonate).
Aveti grija, daca faceti asta pentru toate planetele o sa dureze, puteti limita scriptul sa ruleze doar pentru cateva planete
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
    """
        :param planet_data accepts a list of tuples in order to extract relevant data
        :return a list of tuples
    """
    resident_list = [("planet: " + str(x['name']), x['residents']) for x in planet_data]
    resident_movies_list = []
    for planet_name, rez_request in resident_list:
        for index, movie_req in enumerate(rez_request, start=1):
            data = requests.get(movie_req)
            response = json.loads(data.text)
            resident_film = response['films']
            resident_film = ("Resident no: {} ".format(index) + "from " + str(planet_name), resident_film)
            resident_movies_list.append(resident_film)
    return resident_movies_list


def get_movie_titles(movie_links):
    """
        Method used in combination with get_residents_films
        :param movie_links is a list of movie links
        :return a list of tuples formed by resident and movie_list
        """
    all_resident_movie_list = []
    for resident, movie_link in movie_links:
        movie_list = _get_titles(movie_link)
        all_resident_movie_list.append((resident, movie_list))
    return all_resident_movie_list


def _get_titles(movie_links):
    """
    :param movie_links must be a list
    Private method used for get_movie_titles
    collect from each response the title of movie and store them in a list
    :return resident_movie_list: as a list"""
    if len(movie_links) > 0:
        resident_movie_list = []
        for movie in movie_links:
            movie_titles = requests.get(movie)
            movie_titles = json.loads(movie_titles.text)
            resident_movie_list.append(movie_titles['title'])
    return resident_movie_list


if __name__ == "__main__":
    """Returns a list of tuples with the name of planets and the corresponding residents"""
    planets_data = get_data_for_num_of_planets(1)
    print(len(planets_data))
    residents_movie = get_residents_films(planets_data)
    [print(x) for x in get_movie_titles(residents_movie)]
    # pprint.pprint(get_planet_name_and_residence_num(planets_data))
