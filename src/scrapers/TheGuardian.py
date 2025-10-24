from src.scrapers.base import BaseScraper
from src.models.Article import Article

class TheGuardian:

    def __init__(self):
        self.__base_url = 'https://www.theguardian.com/international'

    def extract(self):
        main_page = BaseScraper(self.__base_url)
        main_page.load_page()
        articles = []

        return articles
