from src.scrapers.BBC import BBC

class Main:

    def __init__(self):
        pass

    @staticmethod
    def start():
        bbc_scraper = BBC()
        articles = bbc_scraper.extract()

        for article in articles:
            print(article)


if __name__ == '__main__':
    app = Main()
    app.start()
