from db.transactions.DBManager import DBManager
import os
__author__ = 'marcelo_garay'


class TransactionManager(object):

    def __init__(self):
        """
        Create connection with data base sqlite
        :return:
        """
        self.conn = DBManager()

    def get_users(self):
        """
        Get list of users
        :return:
        """
        for row in self.conn.query("select * from user"):
            print type(row)
            print row


if __name__ == "__main__":
    TransactionManager().get_users()
