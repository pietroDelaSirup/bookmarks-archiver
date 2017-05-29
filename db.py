import psycopg2  # for postgres
import datetime

class DB:
    """working with postgres db"""

    def __init__(self):
        # postgres db connection
        postgre_str = "dbname='browser_history' user='postgres' host='localhost' password='postgres'"
        self.conn = psycopg2.connect(postgre_str)
        self.cursor = self.conn.cursor()

        self.seq = 0


    def get_next_val(self):
        self.cursor.execute("SELECT nextval('id')")
        return self.cursor.fetchone()[0]


    def save(self, urls):
        id = self.get_next_val()

        for url in urls:
            self.cursor.execute(
                "INSERT INTO bookmarks(id, url, create_date)VALUES("'%s' + ',%s' + ',%s'")",
                (id , url, datetime.datetime.utcnow())
            )
            id += 1
            self.conn.commit()

        self.cursor.execute("ALTER SEQUENCE id RESTART WITH " + str(id))
        self.conn.commit()


    def cleanup(self):
        self.cursor.close()




