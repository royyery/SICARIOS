__author__ = 'alex alvarez'

import unittest
from admin_module.user_module.system_user import SystemUser


class TestSystemUser(unittest.TestCase):
    def test_new_system_user_is_an_system_user_instance(self):
        first_name = "Alex"
        last_name = "Alvarez"
        system_user = SystemUser(first_name, last_name, "AJA-01")
        self.assertIsInstance(system_user, SystemUser)

    def test_new_instance_is_created_with_first_name(self):
        first_name = "Alex"
        last_name = "Alvarez"
        system_user = SystemUser(first_name, last_name, "AJA-01")
        self.assertEqual(first_name, system_user.get_first_name())

    def test_new_instance_is_created_with_last_name(self):
        first_name = "Alex"
        last_name = "Alvarez"
        system_user = SystemUser(first_name, last_name, "AJA-01")
        self.assertEqual(last_name, system_user.get_last_name())

    def test_new_instance_is_created_with_code(self):
        first_name = "Alex"
        last_name = "Alvarez"
        system_user = SystemUser(first_name, last_name, "AJA-01")
        self.assertEqual("AJA-01", system_user.get_code())