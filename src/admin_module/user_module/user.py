from person import Person
from sellrent import SellRent
from getaccess import GetAccess
from buildreport import BuildReport


__author__ = 'Amilcar Maida'


class User(Person):
    """
    User class allows rent, sell and generate reports about movies available
     :method rent_movie: define the functionality to rent movies
     :method sell_movie: define the functionality to sell movies
     :method generate_report: define the functionality to generate reports
     :method return_movie: define the functionality to return movies
     :method login_user: define the functionality to get access to rent and sell
    """
    def __init__(self, first_name, last_name, role, user_name, password):
        """
        Initialize User class
        :param first_name: String
        :param last_name: String
        :param role: String
        :param user_name: String
        :param password: String
        """
        self.role = role
        self.password = password
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        Person.__init__(self, first_name, last_name)

    def login_user(self, user_name, password):
        """
        Method to verify if user exists and its correct
        """

        get_access = GetAccess(user_name, password)
        if get_access.login_init():
            """
            :method get_access.login_init: verify if user is registered
            """
            if self.user_name == user_name and self.password:
                self.in_use = True
                return True
            else:
                return False
        else:
            return False

    def sell_movie(self, user_name, password, role, movie_code):
        """
        Method to sell movies
        """

        if User.login_use(user_name, password):
            if role == self.role == 'Administrator' or role == self.role == 'Employee':
                SellRent.sell_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to sell movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def rent_movie(self, role, user_name, password, movie_code):
        """
        Method to rent movies
        """

        if User.login_use(user_name, password):
            if role == self.role == 'Administrator' or role == self.role == 'Employee':
                SellRent.rent_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to rent movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def return_movie(self, user_name, password, role, movie_code):
        """
        Method to return movies
        """

        if User.login_use(user_name, password):
            if role == self.role == 'Administrator' or role == self.role == 'Employee':
                SellRent.return_a_movie(movie_code)
                return True
            else:
                print "You must be the Administrator or Employee to be able to return movies"
        else:
            print "User or password incorrect, please try with valid credentials"

    def generate_report(self, user_name, password, role):
        """
        Method to generate reports
        """

        if User.login_use(user_name, password):
            if role == self.role == 'Administrator' or role == self.role == 'Employee':
                BuildReport.build_report()
            else:
                print "You must be the Administrator or Employee to be able to generate reports"
        else:
            print "User or password incorrect, please try with valid credentials"


