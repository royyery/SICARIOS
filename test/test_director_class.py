__author__ = 'alex alvarez'

import unittest
from admin_module.user_module.director import Director
from admin_module.movie import Movie


class TestDirector(unittest.TestCase):
    def test_director_is_a_new_instance_director_class(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertIsInstance(director, Director);

    def test_create_new_director_intance_with_first_name(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertEqual(director.get_first_name(), first_name);

    def test_create_new_director_intance_with_second_name(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertEqual(director.get_second_name(), second_name);

    def test_add_a_movie_to_director_filmography_list(self):
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        movie = Movie()
        director.add_movie_to_filmography(movie)
        self.assertTrue(movie, director.diricted_the_film(movie))


if __name__ == "__main__":
    unittest.main();
