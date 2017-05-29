import re

class Reader:
    """read data for chrome browser from bookmarks file"""

    def __init__(self):
        self.urls = self.read_urls_from_file()


    def get_urls(self):
        return self.urls


    def read_urls_from_file(self):
        file = open("Bookmarks", encoding="utf8")
        encode_file = file.read()
        urls = re.findall("http[\:\/\.a-zA-Z0-9\-\?\=\&]+", encode_file)
        return urls


