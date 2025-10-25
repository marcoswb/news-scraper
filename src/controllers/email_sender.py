import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.controllers.enviroments import get_env


class Emailsender:

    def __init__(self):
        self.__sender = get_env('SENDER')
        self.__password = get_env('PASSWORD')
        self.__receiver = get_env('RECEIVER')
        print(self.__sender)

    def send_email(self, portal_name, articles:list):
        if not articles:
            return

        html = f'<h2>{portal_name} - Daily English News</h2>'
        for article in articles:
            text = ''
            for p in article.get_paragraphs():
                text += f'<p>{p}</p>'

            html += f"""
            <details>
                <h2><b><a href="{article.get_link()}">{article.get_title()}</a></b></h2>
                <summary>{text}</summary>
            </details>
            <hr>
            """

        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'{portal_name} - Daily English News'
        msg['From'] = self.__sender
        msg['To'] = self.__receiver
        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.__sender, self.__password)
            server.send_message(msg)
