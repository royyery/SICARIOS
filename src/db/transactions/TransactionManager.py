from db.transactions.DBManager import DBManager

__author__ = 'marcelo_garay'


class TransactionManager(object):
    db_name = "sicarios"

    def __init__(self):
        """
        Create connection with data base sqlite
        :return:
        """
        self.conn = DBManager(self.db_name)

    def get_users(self):
        """
        Get list of users
        :return:
        """
        for row in self.conn.query("select * from user"):
            print row


if __name__ == "__main__":
    TransactionManager().get_users()
