import requests
from urllib.parse import quote, urlparse
from bs4 import BeautifulSoup



class SearchResultsPage:
    def __init__(self, query):
        self.query = quote(query)


    def results(self):
        results = []
        for soup_node in self.__get_reults_soup():
            link = soup_node.find("a", class_="result__a")

            results.append({
                'link': link.get('href'),
                'title': link.text,
                'domain': urlparse(link.get('href')).netloc,
                'description': soup_node.find('a', class_='result__snippet').text
            })

        return results


    def __get_reults_soup(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
        }

        url  = 'https://html.duckduckgo.com/html/?q='+self.query+'&lang=en-us'
        page = requests.get(url, headers=headers).text

        return BeautifulSoup(page, 'html.parser').find_all('div', class_='result results_links results_links_deep web-result')
