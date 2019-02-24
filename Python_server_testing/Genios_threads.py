from timeit import default_timer as timer

import bs4
import urllib.request
import ConfigData as config_data
from multiprocessing import Process
from Python_files_manipulation.CSVManipulation import CSVManipulation as csv_manipulation

conf_data = config_data.ConfigData.get_instance()
cube_types_file = conf_data.get_value(config_data.CUBE_TYPES_CSV)
URL_lists = csv_manipulation(cube_types_file).read_csv_specific_column(1)


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



