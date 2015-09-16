__author__ = 'alex alvarez'

from person import Person
from utils.util import search_movie_in_filmography


class Director(Person):
    """
    Create an instance of Director class
    it will contain director data of a movie
    Director class extends from Person class, attibute 'filmography' keeps a movies list
    that were directed by this director
    """
    def __init__(self, first_name, last_name):
        """
        Extends from Person.__init__() to store common data of a person

        """
        Person.__init__(self, first_name, last_name)
        self._filmography = []
        """Store movies in a list"""

    def add_movie_to_filmography(self, movie):
        """
        Add a movie that was directed by this director to filmography list
        :param movie: movie that was directed by this director
        :return: True if movie was added to director's filmography otherwise False
        """

        if not search_movie_in_filmography(movie, self._filmography):
            self._filmography.append(movie)
            return True
        else:
            print("The movie \'%s\' already exists in director filmography" % movie.title)
            return False

    def get_filmography_list(self):
        """
        Get the movies that were directed by this director
        :return: movies list in _.filmography list
        """
        return self._filmographhy

    def get_movie(self, movie):
        """
        Return a movie from filmography list
        :param movie:
        :return:a movie
        """
        return filter(lambda x: x.code == movie.code, self._filmography)
