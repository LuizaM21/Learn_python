"""Retrieve the most visited links from the wikipedia main site"""

import json
import requests
import bs4

base_url = "http://wikipedia.com"
QUEUE = set([base_url])
MAX_CRAWL = 3
URL_SEEN = set()


def get_page(url):
    # TODO: define a context manager for HTML reading
    response = requests.get(url)
    response.raise_for_status()
    if 'text/html' in response.headers['Content-Type']:
        return bs4.BeautifulSoup(response.text, features="lxml")
    raise ValueError('Not a valid HTML page.')


def parse_links(link_url, soup):
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href:
            continue
        if href.startswith('//'):
            # full url but requires the same scheme
            scheme = requests.compat.urlparse(link_url).scheme
            following_link = scheme + ':' + href

        elif bool(requests.compat.urlparse(href).netloc):
            # full url
            following_link = href

        else:
            # relative url
            following_link = requests.compat.urljoin(link_url, href)

        if following_link not in URL_SEEN:
            QUEUE.add(following_link)


if __name__ == '__main__':
    print(get_page(base_url).prettify())
    print(parse_links(base_url, get_page(base_url)))

