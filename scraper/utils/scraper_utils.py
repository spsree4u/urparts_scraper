
import requests
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, url):
        self.response = requests.get(url)
        self.scraper = BeautifulSoup(self.response.content, "html.parser")

    def get_data_list(self, property_map):
        data_list = []
        div_data = self.scraper.find("div", property_map)
        if div_data:
            ul_data = div_data.find('ul')
            if ul_data:
                for li_data in ul_data.find_all("li"):
                    data_list.append(li_data.text.strip())

        return data_list


# url = "https://www.urparts.com/index.cfm/page/catalogue/JCB/Backhoe%20Parts"
# s = Scraper(url)
# print(s.get_data_list({'class': 'c_container allmodels'}))
