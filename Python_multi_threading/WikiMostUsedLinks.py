"""Retrieve the most visited links from the wikipedia main site"""

import json
import requests
import bs4

base_url = "http://wikipedia.com"


def get_page():
    response = requests.get(base_url)
    response.raise_for_status()
    if 'text/html' in response.headers['Content-Type']:
        return bs4.BeautifulSoup(response.text, features="lxml")
    raise ValueError('Not a valid HTML page.')


if __name__ == '__main__':
    print(get_page())

