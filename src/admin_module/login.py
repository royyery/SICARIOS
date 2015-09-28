__author__ = 'aj'

from utils.util import get_user_from_xml_file

class Login(object):
    """
    Create an instance of Login class
    it allows to login an system user
    attribute credentials will store the user crendentials (account name and password),
    _text attribute store the output labels to retrieve data from console
    """

    def __init__(self):
        """
        :param credentials: dictionary that will store the system user credentials: account name and password
        :param _output_label: dictionary that will store the output labels displayed in console to retrieve system user credentials
        :return: none
        """
        self.credentials = {"account": None, "password": None}
        self._output_label = {'account': "Insert user account: ",
                              'password': "Insert your password: "}

    def is_text_empty(self, entry):
        """
        Validate if text in entry parameter is empty
        :param entry: string type tha will be validated in order to know if is empty ("")
        :return: return True if "entry" is "", False otherwise
        """
        return entry.strip() == ""

    def get_user_credentials(self):
        """
        Retrieve system user credentials from console
        :return: None
        """
        for key in self._output_label:
            """ iterate through _output_label to display labels in console """
            entry_saved = False
            while not entry_saved:
                """ display same label while the user entering empty string """
                entry = raw_input(self._output_label[key])
                entry_saved = self.save_entry(entry, key)

    def save_entry(self, entry, key):
        """
        Will save the entry string in the _credentials dictionary in the 'key' position
        :param entry: string that will be saved in the _credentials dictionary
        :param key: string that indicates the position for the dictionary
        :return: True if entry was saved in _credentials dictionary, False otherwise
        """
        if self.is_text_empty(entry):
            """ validates if string in text is empty """
            return False
        self.credentials[key] = entry
        return True

    def authenticate_credentials(self):
        """
        Will return True if credentials match with user data obtained from get_user_from_file method
        :return: True if user account and password obtained from users.xml file matchs with entered credentials, False otherwise
        """
        existing_user = get_user_from_xml_file(self.credentials['account'])
        """ get an user from users.xml file that match with stored credentials """
        if existing_user is not None and existing_user[1][1] == self.credentials['password']:
            return True

    def print_credentials(self):
        """
        print the stored credentials in console
        :return: None
        """
        for key in self._output_label:
            print self.credentials[key]


