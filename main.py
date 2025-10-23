from src.scrapers.BBC import BBC

class Main:

    def __init__(self):
        pass

    @staticmethod
    def start():
        bbc_scraper = BBC()
        bbc_scraper.extract()


if __name__ == '__main__':
    app = Main()
    app.start()
