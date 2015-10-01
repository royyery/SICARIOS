__author__ = 'Amilcar Maida'


import sys
import os
from menuadministrator import MenuAdministrator 
from menuemployee import MenuEmployee 
from menuvisitor import MenuVisitor 
from login import Login


#class Login:
#    def read_user(self):
#        self.user_name = raw_input("Enter the user name: ")
#        self.password = raw_input("Enter the password: ")
#    
#    def validate_user(self, user, password):
#        #connect and ask to database if user exist
#        #user, password, role = #retrieved from datbase
#        if self.user_name == user and self.password == password:
#            return True

class MainClass:
    """
    Main Class alloes start and end the application.
    Also it will let us display the different menus for different users: 
    Administrator, Employee, Visitor and Customer  
    """
    
    def main(self):
        """
        :cls: Allows clean the console window
        :read_user: Allows ask the user and password
        :display menu: Allows to show different menus for different users:
        Administrator, Employee, Visitor and Customer
        """
        self.cls()
        
        
        
#        login = Login()
#        login.read_user()
#        user_name = "Pedro"
#        password = "Control123"
#        role = "Visitor"
        login_init = Login()
        if login_init.init_session():
            if login_init.get_session_user_role() == "Administrator":
                self.cls()
                mainmenu = MenuAdministrator()                
                mainmenu.display_menu()
            elif login_init.get_session_user_role() == "Employee":
                self.cls()
                mainmenu = MenuEmployee()                
                mainmenu.display_menu()
            elif login_init.get_session_user_role() == "Visitor":
                self.cls()
                mainmenu = MenuVisitor()                
                mainmenu.display_menu()            
    
    def cls(self):
        os.system(['clear','cls'][os.name == 'nt'])
                        

main = MainClass()
main.main()
        

    