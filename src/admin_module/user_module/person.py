__author__ = 'alex alvarez'


class Person(object):
    def __init__(self, first_name, second_name):
        self._first_name = first_name
        self._second_name = second_name

    def get_first_name(self):
        return self._first_name

    def get_second_name(self):
        return self._second_name


