#!/usr/bin/env python

import json
import sys

import requests

BASE_URL = "https://swapi.co/"


def get_planets_data():
    """Return all the StartWars planets."""
    # get the planets data
    url_to_call = requests.compat.urljoin(BASE_URL, "/api/planets")
    full_data = []
    while True:
        print("Calling page: ", url_to_call)
        planets_result_raw = requests.get(url_to_call)

        if not planets_result_raw.ok:
            print("Am primit status code ", planets_result_raw.status_code)
            sys.exit(1)

        planets_json = json.loads(planets_result_raw.text)
        full_data.extend(planets_json['results'])

        next_page = planets_json.get('next', None)
        if next_page is None:
            # am ajuns la final
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


def main():
    """Main entry point of the program."""
    planets_data = get_planets_data()

    # planets_and_residents = [
    #     (item['name'], len(item['residents']),
    #      [get_name(url) for url in item['residents']]) for item in planets_data
    # ]

    planets_and_residents = []
    for planet in planets_data:
        name = planet['name']
        residents_count = len(planet['residents'])

        residents_names = []
        for url in planet['residents']:
            residents_names.append(get_name(url))

        planets_and_residents.append((name, residents_count, residents_names))

    planets_and_residents.sort(key=lambda x: x[1], reverse=True)

    for name, residents_count, residents in planets_and_residents:
        print("{:15} -> {}".format(name, residents_count))

        for name in residents:
            print("\t - ", name)

    print("\n\n\nPlanets with more then on resident\n")

    # more_then_1 = filter(lambda x: x[1] > 1, planets_and_residents)
    more_then_1 = [x for x in planets_and_residents if x[1] > 1]
    for name, residents_count, residents in more_then_1:
        print("{:15} -> {}".format(name, residents_count))

        for name in residents:
            print("\t - ", name)


if __name__ == "__main__":
    main()
