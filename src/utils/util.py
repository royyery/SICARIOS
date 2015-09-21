__author__ = 'aj'


def search_movie_in_filmography(criteria, filmography):
    """
    Search a movie in filmography list by using the criteria parameter, if exist return the movie
    :param criteria: dictionary that store the search criteria, code or title of the movie
    :param filmography: movie list where will search a movie according criteria
    :return: return a movie object that was found in the filmography list
    """

    if criteria.keys() == ['code']:
        """ search a movie in filmography list by code """
        for index in range(0, len(filmography)):
            if filmography[index].code == criteria['code']:
                print type(filmography[index])
                return filmography[index]

    if criteria.keys() == ['title']:
        """ search a movie in filmography list by title """
        for index in range(0, len(filmography)):
            if filmography[index].title == criteria['title']:
                print type(filmography[index])
                return filmography[index]