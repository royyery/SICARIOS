__author__ = 'Amilcar Maida'


class AccessDB(object):
    """Class that allows implement the login functionality"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def search_user(self, user_name):
        if self.user_name == user_name:
            return True
        else:
            return False

