__author__ = 'aj'


def search_movie_in_filmography(movie, filmography):
    """
    Search a movie by code in filmography list, if exist return the movie
    :param movie:
    :param filmography:
    :return: return the movie that was found in the filmography list
    """
    return filter(lambda x: x.code == movie.code, filmography)
