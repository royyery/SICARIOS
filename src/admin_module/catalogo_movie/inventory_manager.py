__author__ = 'Ariel'
from src.db.transactions.connection import *

class Inventory_Queries:

    def __init__(self):
        self.database = DatabaseManager()

    def get_availability_for_rent(self, movie_title):
        self.database.run_query('SELECT quantity_for_rent FROM Movie WHERE movie_name ="%s" and quantity_for_rent != 0'%movie_title)
        data = self.database.cursor.fetchall()
        if data:
            return True
        else:
            return False

    def get_availability_for_sell(self, movie_title):
        self.database.run_query('SELECT quantity_for_sell FROM Movie WHERE movie_name ="%s" and quantity_for_sell != 0'%movie_title)
        data = self.database.cursor.fetchall()
        if data:
            return True
        else:
            return False

    def get_amount_movies_for_rent(self, movie_name):
        self.database.run_query('SELECT quantity_for_rent FROM Movie WHERE movie_name = "%s"'%movie_name)
        movie_tuples = self.database.cursor.fetchall()
        for movie_amount in movie_tuples:
            return movie_amount[0]

    def get_amount_movies_for_sell(self, movie_name):
        self.database.run_query('SELECT quantity_for_sell FROM Movie WHERE movie_name = "%s"'%movie_name)
        movie_tuples = self.database.cursor.fetchall()
        for movie_amount in movie_tuples:
            return movie_amount[0]

    def query_update_movie_rented(self, movie, new_amount):
        self.database.run_query('UPDATE Movie SET quantity_for_rent = %s WHERE movie_name = "%s"'%(new_amount, movie))

    def query_update_movie_sold(self, movie, new_amount):
        self.database.run_query('UPDATE Movie SET quantity_for_sell = %s WHERE movie_name = "%s"'%(new_amount, movie))
