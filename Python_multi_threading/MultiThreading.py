import threading
import time
import requests

class MultiThreadingCalc(threading.Thread):
    def __init_(self, name, sleep_time):
        self.name = name
        self.sleep = sleep_time

    _sum = 0

    def run(self):
        global _sum
        time.sleep(self.sleep)
        _sum = _sum + self.name
        to_print = "{} {}".format(self.name, _sum)
        print(to_print)


class WikiThread:
    base_url = 'https://en.wikipedia.org/wiki/Main_Page'

    def count_words(self, text):
        words = {}
        for word in text.split():
            if word not in words.keys():
                words[word] = words[word] + 1

    def crawl_web(self):
        response = requests.get(self.base_url)
        if response.ok:
            content = response.text
            print(content)


if __name__ == '__main__':
    th_1 = MultiThreadingCalc(1)

