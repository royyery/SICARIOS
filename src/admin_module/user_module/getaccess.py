from accessdb import AccessDB


__author__ = 'Amilcar Maida'


class GetAccess(object):
    """Class that allows implement the login functionality"""
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def login_init(self):

        access_db = AccessDB(self.user_name, self.password)
        if access_db.search_user(self.user_name):
            return True
        else:
            return False
