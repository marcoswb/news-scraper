from src.scrapers.base import BaseScraper
from src.models.Article import Article

class CBC:

    def __init__(self):
        self.__base_url = 'https://www.cbc.ca'

    def extract(self):
        main_page = BaseScraper(f'{self.__base_url}/news')
        main_page.load_page()
        articles = []

        for item in main_page.get_itens('a.cardText'):
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

            article = Article()
            article.set_link(url)

            article_page = BaseScraper(url)
            article_page.load_page()

            div_title = article_page.get_itens('h1.detailHeadline')
            if div_title:
                article.set_title(div_title[0].get_text(strip=True))
            else:
                continue

            divs_text = article_page.get_itens('.story > p, .story > h2')
            for paragraph in divs_text:
                article.add_text(paragraph)

            articles.append(article)
            if len(articles) == 5:
                break

        return articles
