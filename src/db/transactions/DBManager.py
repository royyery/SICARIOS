import sqlite3
__author__ = 'marcelo_garay'


class DBManager(object):
    def __init__(self, db):
        """
        Make connection to an SQLite database file
        :param db:
        :return:
        """
        self.conn = sqlite3.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        """
        Execute a query
        :return
        """
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def close(self):
        """
        Close connection to the database
        """
        self.conn.close()
