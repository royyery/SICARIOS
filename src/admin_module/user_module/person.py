import random
import null as null

__author__ = 'Marcelo Garay'
__author__ = 'Amilcar Maida'
__author__ = 'Alex Alvarez'


class Person(object):
    """
    Person class cna get, set the name and last name. It will add, update 
    or delete the person.
    """

    def __init__(self, first_name, last_name):
        """
        Initialize first_name and last_name
        :param first_name: String
        :param last_name: String
        :return:
        """
        self._first_name = first_name
        self._last_name = last_name
        self._code = "123456"

    def get_first_name(self):
        """
        Get Name
        :return: String
        """
        return self._first_name

    def get_last_name(self):
        """
        Get Last name
        :return: String
        """
        return self._last_name

    def set_first_name(self, name):
        """
        Set Name over the person created
        :param name:  String
        :return: void
        """
        self._first_name = name

    def set_last_name(self, last_name):
        """
        Set Last name over the person created
        :param last_name: String
        :return: void
        """
        self._last_name = last_name

    def remove(self):
        """
        Person is removeed
        :return:
        """
        self._first_name = null
        self._last_name = null
        self._code = 0
