import threading
import time
import requests

_sum = 0


class MultiThreadingCalc(threading.Thread):
    def __init__(self, name, lock, sleep_time=2):
        super(MultiThreadingCalc, self).__init__()
        self._name = name
        self._sleep = sleep_time
        self._lock = lock

    def run(self):
        global _sum
        time.sleep(self._sleep)
        to_print = "{} {}".format(self._name, time.time())

        self._lock.acquire()
        print(to_print)
        _sum = _sum + self.name
        to_print = "{} S: {}".format(self.name, _sum)
        print(to_print)
        self._lock.release()


def main():
    print("Create threads")
    lock = threading.Lock()
    threads = []
    for i in range(5):
        th = MultiThreadingCalc(i, lock, 1)
        threads.append(th)
        th.start()
        th.join()


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
    main()

