import bs4
import requests
import pprint

base_url = "https://www.genios.ro/"


class GeniosServer:
    """Get a valid site and execute a request for that site"""
    def __init__(self, url):
        self.site_url = url
        self.site_link = []
        self.site_response = requests.get(self.site_url)

    def get_page_content(self):
        """Loads content of the first page of a site"""
        response = self.site_response
        response.raise_for_status()
        if 'text/html' in response.headers['Content-Type']:
            return bs4.BeautifulSoup(response.text, features="html.parser").prettify()
        raise ValueError('Not a valid HTML page.')

    def get_response_headers(self):
        """Return header data of the server"""
        header = self.site_response.headers
        return header

    def get_site_link_lists(self):
        """Return all the visible links from the current site"""
        site_content = bs4.BeautifulSoup(self.site_response.text, features="html.parser")
        for link in site_content.find_all("a"):
            href = link.get('href')
            if href.startswith("http"):
                self.site_link.append(href)
            else:
                continue
        return self.site_link

    def get_all_cubes_types(self):
        """Return all the cube models from the front page"""
        site_content = bs4.BeautifulSoup(self.site_response.text, features="html.parser")
        menu_list = site_content.findAll("ul", attrs={'id': 'menu-marci'})[0].findAll("li")
        return menu_list


if __name__ == '__main__':
    site = GeniosServer(base_url)

    # content_site = site.get_page_content()
    # print(content_site)
    # site_header = site.get_response_headers()
    # pprint.pprint(site_header)
    # pprint.pprint(site.get_site_link_lists())

    [print(x) for x in site.get_all_cubes_types()]



