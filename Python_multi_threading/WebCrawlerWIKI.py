#!/usr/bin/env python3
"""Pastebin quotes generator."""
from __future__ import print_function

import json
import threading
import time
import pprint
import requests
import bs4

START_URL = "http://wikipedia.com"
QUEUE = {START_URL}
MAX_CRAWL = 10
NR_THREADS = 5
THREADS = []
URL_SEEN = set()


def get_page(url):
    response = requests.get(url)
    response.raise_for_status()
    if 'text/html' in response.headers['Content-Type']:
        return bs4.BeautifulSoup(response.text, features="lxml")
    raise ValueError('Not a valid HTML page.')


def parse_links(url, soup):
    for link in soup.find_all('a'):
        href = link.get('href')

        if not href:
            continue

        if href.startswith("//"):
            # full url but requires the same scheme
            scheme = requests.compat.urlparse(url).scheme
            following_link = scheme + ':' + href

        elif bool(requests.compat.urlparse(href).netloc):
            # full url
            following_link = href

        else:
            # relative url
            following_link = requests.compat.urljoin(url, href)

        if following_link not in URL_SEEN:
            QUEUE.add(following_link)


class Spider(threading.Thread):
    """Spider thread."""
    # overwrite the init function of threads
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.data = {}

    def run(self):
        print("Start working ", self.name)
        while len(self.data) < MAX_CRAWL / NR_THREADS:
            url = None
            if self.queue:
                url = self.queue.pop()
            else:
                time.sleep(1)

            if url in URL_SEEN or url is None:
                continue
            print("{:5} - [{:3} from {:4}]Crawl {:} ...".format(
                self.name, len(self.data), len(self.queue), url[:-100]), end="")

            try:
                page = get_page(url)
            except Exception as exc:
                print("Skip :", exc)
                continue

            # count the number of charts
            content_len = len(page.text)
            self.data[url] = content_len
            # retrieve all the links and set them into a queue
            parse_links(url, page)

            print(" has ", content_len)
        print("Stop working", self.name)


def main():
    """Starting point."""
    for index in range(NR_THREADS):
        spider = Spider("s" + str(index), QUEUE)
        THREADS.append(spider)

    # star in parallel multi threading
    for thread_s in THREADS:
        thread_s.start()

    data = dict()
    for thread_j in THREADS:
        thread_j.join()
        data.update(thread_j.data)
        # print("Data [{}] : {}".format(thread_j.name, thread_j.data))

    pprint.pprint(data)
    with open("data.json", "w") as fd:
        fd.write(json.dumps(data))


if __name__ == '__main__':
    main()
