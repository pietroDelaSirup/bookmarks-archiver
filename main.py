from reader import Reader
from db import DB

class Main:

    def __init__(self):
        reader = Reader()
        urls = reader.get_urls()
        database = DB()
        database.save(urls)
        database.cleanup()
