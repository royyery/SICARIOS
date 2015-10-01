from db.transactions.DBManager import DBManager

__author__ = 'marcelo_garay'


class TransactionManager(object):
    db_name = "sicarios"

    def simple(self):
        db = DBManager(self.db_name)
        for row in db.query("select * from user"):
            print row


if __name__ == "__main__":
    TransactionManager().simple()
