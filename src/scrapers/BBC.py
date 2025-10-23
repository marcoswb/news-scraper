from src.scrapers.base import BaseScraper

class BBC:

    def __init__(self):
        self.__base_url = 'https://www.bbc.com'

    def extract(self):
        main_page = BaseScraper(self.__base_url)
        main_page.load_page()

        for item in main_page.get_itens('a.sc-8a623a54-0'):
            link = str(item['href'])
            if main_page.is_link(link):
                if link.startswith(self.__base_url):
                    check_url = link.replace(self.__base_url, '')
                    if not main_page.is_internal_link(check_url):
                        continue

                url = str(link)
            elif main_page.is_internal_link(link):
                url = f'{self.__base_url}{link}'
            else:
                continue

            if not url.startswith(self.__base_url):
                continue

            print(url)
