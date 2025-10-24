from src.scrapers.BBC import BBC
from src.controllers.email_sender import Emailsender

class Main:

    def __init__(self):
        self.__email_sender = Emailsender()

    def start(self):
        bbc_scraper = BBC()
        articles = bbc_scraper.extract()

        self.__email_sender.send_email('BCC', articles)


if __name__ == '__main__':
    app = Main()
    app.start()
