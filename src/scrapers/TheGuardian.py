from src.scrapers.base import BaseScraper
from src.models.Article import Article

class TheGuardian:

    def __init__(self):
        self.__base_url = 'https://www.theguardian.com'
        self.__articles_titles = []

    def extract(self):
        main_page = BaseScraper(f'{self.__base_url}/international')
        main_page.load_page()
        articles = []

        for item in main_page.get_itens('a.dcr-2yd10d'):
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

            if not url.startswith(f'{self.__base_url}/world/'):
                continue

            article = Article()
            article.set_link(url)

            article_page = BaseScraper(url)
            article_page.load_page()

            div_title = article_page.get_itens('h1.dcr-1k1a1x')
            if div_title:
                article.set_title(div_title[0].get_text(strip=True))
            else:
                continue

            if article.get_title() in self.__articles_titles:
                continue

            divs_text = article_page.get_itens('p.dcr-130mj7b')
            if not divs_text:
                continue

            for paragraph in divs_text:
                article.add_text(paragraph)

            articles.append(article)
            self.__articles_titles.append(article.get_title())
            if len(articles) == 5:
                break

        return articles
