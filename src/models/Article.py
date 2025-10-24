class Article:

    def __init__(self):
        self.__title = None
        self.__text = []
        self.__link = None

    def set_title(self, title):
        self.__title = title

    def add_text(self, text):
        self.__text.append(text)

    def set_link(self, link):
        self.__link = link

    def __str__(self):
        return f'title: {self.__title}\nlink: {self.__link}\ntext: {"\n".join(self.__text)}\n'