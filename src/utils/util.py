__author__ = 'aj'


def search_movie_in_filmography(criteria, filmography):
    """
    Search a movie in filmography list by using the criteria parameter, if exist return the movie
    :param criteria: dictionary that store the search criteria, code or title of the movie
    :param filmography: movie list where will search a movie according criteria
    :return: return a movie object that was found in the filmography list
    """
    for index in range(0, len(filmography)):
        if filmography[index].__dict__[criteria.keys()[0]] == criteria[criteria.keys()[0]]:
            return filmography[index]
