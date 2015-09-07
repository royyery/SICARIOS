__author__ = 'alex alvarez'

import unittest
from admin_module.user_module.director import Director


class TestDirector(unittest.TestCase):
    def test_director_is_a_new_instance_director_class(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertIsInstance(director, Director);

    def test_create_new_director_intance_with_first_name_and_second_name(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertEqual(director.get_first_name(), first_name);
        self.assertEqual(director.get_second_name(), second_name);


if __name__ == "__main__":
    unittest.main();
