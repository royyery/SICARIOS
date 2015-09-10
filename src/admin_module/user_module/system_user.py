__author__ = 'alex alvarez'

from admin_module.user_module.person import Person


class SystemUser(Person):
    """
    SystemUser extends from Person
    attributes class store data from users that access to system
    """
    def __init__(self, first_name, second_name, code):
        """
        Extends from Person.__init__() to store common data of a person
        :return: none
        """
        Person.__init__(self, first_name, second_name)
        self.code = code
        self.birth_date = None
        self.address = None
        self.phone_number = []
        self.email = None
        self.role = None

    def set_birth_date(self, birth_date):
        """
        set the birth_date of the user
        :param birth_date:
        :return:
        """
        self.birth_date = birth_date

    def set_address(self, address):
        """
        set the address
        :param address:
        :return: none
        """
        self.address = address

    def set_phone_number(self, number):
        """
        set the user phone number(s)
        :param number:
        :return: none
        """
        self.phone_number.append(number)

    def set_email(self, email):
        """
        set user email
        :param email:
        :return:
        """
        self.email = email

    def set_role(self, role):
        """
        set the user role
        :param role:
        :return: none
        """
        self.role = role


