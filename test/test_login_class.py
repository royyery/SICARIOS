__author__ = 'aj'


import unittest
from admin_module.login import *


class TestLogin(unittest.TestCase):
    def test_new_login_object_is_an_instance_of_Login_class(self):
        login = Login()
        self.assertIsInstance(login, Login)


