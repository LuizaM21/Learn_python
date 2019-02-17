from timeit import default_timer as timer

import bs4
import urllib.request
from multiprocessing import Process


URL_lists = ['https://www.genios.ro/catalog/moyu/',
             'https://www.genios.ro/catalog/lanlan/',
             'https://www.genios.ro/catalog/philos/',
             'https://www.genios.ro/catalog/mefferts/',
             'https://www.genios.ro/catalog/mofangge/',
             'https://www.genios.ro/catalog/shengshou/',
             'https://www.genios.ro/catalog/yj/',
             'https://www.genios.ro/catalog/yuxin/',
             'https://www.genios.ro/catalog/mf8/',
             'https://www.genios.ro/catalog/calvin/',
             'https://www.genios.ro/catalog/qiyi/']


def get_page_content(site_url):
    """Loads html content of the site"""
    with urllib.request.urlopen(site_url) as response:
        if 'text/html' in response.headers['Content-Type']:
            current_header = bs4.BeautifulSoup(response.read(), features="html.parser").find(id="header")
            return current_header
        raise ValueError('Not a valid HTML page.')


if __name__ == '__main__':

    process_list = []
    for site in URL_lists:

        start_time = timer()
        process = Process(target=get_page_content, args=(site,))
        process_list.append(process)
        process.start()
        end_time = timer()
        duration = end_time - start_time
        print("\ncalled link: {0}\nprocess name: {1}\nprocess duration: {2:.3f}"
              .format(site, process.name, duration))

    for process_ in process_list:
        process_.join()



