from admin_module.user_module.director import Director

__author__ = 'marcelo_garay'


class Movie(object):
    """
    Creation of an instance of movie
    """

    def __init__(self, title, story_line, release_year,
                 id_actor=None, id_director=None):
        self.title = title
        self.story_line = story_line
        self.release_year = release_year
        self.rating = 0
        self.ranking = 0
        self.genres = ""
        self.rental_price = 0
        self.sell_price = 0
        self.quantity_available = []
        self.id_actor = id_actor
        self.id_director = id_director

    def _get_title(self):
        """
        Get Title movie
        :return:
        """
        return self.title

    def _get_story_line(self):
        """
        Get Story line
        :return:
        """
        return self.story_line

    def _get_release_year(self):
        """
        Get Release year
        :return:
        """
        return self.release_year
