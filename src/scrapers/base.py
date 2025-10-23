import requests
from bs4 import BeautifulSoup


class BaseScraper:

    def __init__(self, website_link):
        self.__website_link = website_link
        self.__soup_data = None

    def get_website_link(self):
        return self.__website_link

    def load_page(self):
        html = requests.get(self.get_website_link()).text
        self.__soup_data = BeautifulSoup(html, 'html.parser')

    def get_itens(self, select_item):
        return self.__soup_data.select(select_item)

    @staticmethod
    def is_link(str_link):
        if str(str_link).startswith('http'):
            return True

        return False

    @staticmethod
    def is_internal_link(str_link):
        if str(str_link).startswith('/') and str(str_link).count('/') > 1:
            return True

        return False
