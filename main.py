from src.controllers.email_sender import Emailsender
from src.scrapers.BBC import BBC
from src.scrapers.Reuters import Reuters
from src.scrapers.TheGuardian import TheGuardian

class Main:

    def __init__(self):
        self.__email_sender = Emailsender()

    def start(self):
        bbc_scraper = BBC()
        articles = bbc_scraper.extract()
        self.__email_sender.send_email('BCC', articles)

        reuters_scraper = Reuters()
        articles = reuters_scraper.extract()
        self.__email_sender.send_email('Reuters', articles)

        the_guardian_scraper = TheGuardian()
        articles = the_guardian_scraper.extract()
        self.__email_sender.send_email('The Guardian', articles)


if __name__ == '__main__':
    app = Main()
    app.start()
