from src.scrapers.base import BaseScraper
from src.models.Article import Article

class Reuters:

    def __init__(self):
        self.__base_url = 'https://www.reuters.com/world/'

    def extract(self):
        main_page = BaseScraper(self.__base_url)
        main_page.load_page()
        articles = []

        return articles
