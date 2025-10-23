from src.scrapers.base import BaseScraper

class BBC(BaseScraper):

    def __init__(self):
        super().__init__('https://www.bbc.com')

    def extract(self):
        base_url = self.get_website_link()

        self.load_page()

        for item in self.get_itens('a.sc-8a623a54-0'):
            link = str(item['href'])
            if self.is_link(link):
                if link.startswith(base_url):
                    check_url = link.replace(base_url, '')
                    if not self.is_internal_link(check_url):
                        continue

                url = str(link)
            elif self.is_internal_link(link):
                url = f'{base_url}{link}'
            else:
                continue

            if not url.startswith(base_url):
                continue

            print(url)
