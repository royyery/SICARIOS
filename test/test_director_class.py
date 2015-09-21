__author__ = 'alex alvarez'

import unittest
from admin_module.user_module.director import Director
from admin_module.movie import Movie


class TestDirector(unittest.TestCase):
    """
    TestDirector allows to run unity test for instances of director class
    """
    def test_director_is_a_new_instance_director_class(self):
        """
        Will verify that a new director instance is an instance of Director class
        :return:
        """
        first_name = "Steven"
        last_name = "Spielberg"
        director = Director(first_name, last_name);
        self.assertIsInstance(director, Director);

    def test_create_new_director_instance_with_first_name(self):
        """
        Will verify that a new director instance is created with a first name that inherits from Person class
        :return:
        """
        first_name = "Steven"
        second_name = "Spielberg"
        director = Director(first_name, second_name);
        self.assertEqual(director.get_first_name(), first_name);

    def test_create_new_director_instance_with_last_name(self):
        """
        Will verify that a director instance is created with a last name that inherits from Person class
        :return:
        """
        first_name = "Steven"
        last_name = "Spielberg"
        director = Director(first_name, last_name);
        self.assertEqual(director.get_last_name(), last_name);

    def test_add_a_movie_to_director_filmography_list(self):
        """
        Will verify that a movie can be added to director's filmography,
        :return:
        """
        first_name = "Steven"
        last_name = "Spielberg"
        director = Director(first_name, last_name);
        movie = Movie("J001", "Jaws")
        self.assertTrue(director.add_movie_to_filmography(movie))

    def test_verify_duplicated_movie_cant_be_added_to_filmography(self):
        """
        will verify that a duplicated movie can't be added to director's filmography
        :return:
        """
        first_name = "Steven"
        last_name = "Spielberg"
        director = Director(first_name, last_name);
        movie = Movie("J001", "Jaws")
        director.add_movie_to_filmography(movie)
        self.assertFalse(director.add_movie_to_filmography(movie))

    def test_searching_movie_in_filmography_list_by_movie_title(self):
        title = "Jaws"
        director = Director("Steven", "Spielberg");
        movie = Movie("J001", title)
        director.add_movie_to_filmography(movie)
        existingMovie = director.get_movie({'title': title})
        self.assertEqual(existingMovie.title, title)

    def test_searching_movie_in_filmography_list_by_movie_code(self):
        code = "J001"
        director = Director("Steven", "Spielberg");
        movie = Movie(code, "Jaws")
        director.add_movie_to_filmography(movie)
        existingMovie = director.get_movie({'code': code})
        self.assertEqual(existingMovie.title, code)


if __name__ == "__main__":
    unittest.main();
