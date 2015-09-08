__author__ = 'alex alvarez'

from person import Person


class Director(Person):
    def __init__(self, first_name, second_name):
        Person.__init__(self, first_name, second_name)
        self._filmography = []

    def add_movie_to_filmography(self, movie):
        self._filmography.append(movie)

    def get_filmography_list(self):
        return self._filmographhy

    def diricted_the_film(self, movie):
        return self._filmography.index(movie)
