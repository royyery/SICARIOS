__author__ = 'Roy Ortiz'

import datetime
from datetime import datetime

class Membership(object):
    def __init__(self, type, percent_of_discount, start_date):
        """
        type is a string it stores the membership type
        percent_of_discount is an int value it will store the percentage of discount from 0 to 100
        start_date is a date value to indicate the membership start date
        """
        self._type = type
        self._percent_of_discount = percent_of_discount
        self._start_date = start_date

    def get_type(self):
        """
        Returns the type of membership
        :return: the type name
        """
        return self._type

    def get_discount(self):
        """
        Returns the percentage of discount according the membership type
        :return: the percentage from 0 to 100
        """
        return self._percent_of_discount

    def get_start_date(self):
        """
        Returns the membership start date
        :return: the suscription start date
        """
        return self._start_date

    def calculate_end_date(self, start_date):
        """
        Returns the end date calculated from start date this by adding 6 months
        :return: the membership end date
        """
        end_date = start_date + datetime.timedelta(6*365/12)
        return end_date


