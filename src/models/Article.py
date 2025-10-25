import re
from bs4 import NavigableString

class Article:

    def __init__(self):
        self.__title = None
        self.__text = []
        self.__link = None
        self.__allowed_tags = ['b', 'strong', 'i', 'em', 'blockquote']

    def set_title(self, title):
        self.__title = title

    def add_text(self, paragraph):
        text = self.extract_text_with_format(paragraph)

        if paragraph.name == 'h2':
            text = f'<h3>{text}</h3>'

        self.__text.append(self.format_text(text))

    def set_link(self, link):
        self.__link = link

    def get_title(self):
        return self.__title

    def get_link(self):
        return self.__link

    def get_paragraphs(self):
        return self.__text

    @staticmethod
    def format_text(text):
        new_text = str(text).replace('“', '"').replace('”', '"')
        new_text = re.sub(r'"([^"]+)"', r'<i>"\1"</i>', new_text)

        return new_text

    def extract_text_with_format(self, paragraph):
        result = ''

        for child in paragraph.children:
            if isinstance(child, NavigableString):
                result += str(child)
            elif child.name in self.__allowed_tags:
                inner = self.extract_text_with_format(child)
                result += f"<{child.name}>{inner}</{child.name}>"
            else:
                result += self.extract_text_with_format(child)

        return result

    def __str__(self):
        text = '\n'.join(self.__text)
        return f'title: {self.__title}\nlink: {self.__link}\ntext: {text}\n'