__author__ = 'aj'

from xml.dom import minidom


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


def get_user_from_xml_file(account):
    """
    Will search an account into users.xml file, will return a list of tuples
    :param account: string for search an account into users.xml file
    :return: list of tuples with user data that match with account parameter, None otherwise
    """
    user_data_file = minidom.parse('../db/entities/users.xml')
    """ get user data from users.xml file"""
    users_data = user_data_file.getElementsByTagName('User')
    """ get uses data """

    for user in users_data:
        if user.attributes['account'].value == account:
            return user.attributes.items()
            break
    return None
