import sys

class MenuVisitor:
    #amount_operations = 4
    
    def __init__(self):
        self.options = {"1": "Manage users", "2": "Manage customers", 
              "3": "Manage movies", "4": "Manage operations", "0":"Exit the application"}
        self.methods = {"1":self.manage_users, "2":self.manage_customers, "3":self.manage_movies, "4":self.manage_operations}
        
    def display_menu(self):
        while True:            
            print "Welcome to the Movie store at 123"
            for key in sorted(self.options):
                print "\t" + key +". " + self.options[key]            
                        
            user_input = raw_input("Enter the operation number you want to perform: ")            
            if self.validate_option(user_input):
                self.do_operation(user_input)
            elif user_input == str(0):
                print "Thanks! Come back soon"
                break

    def do_operation(self, user_input):               
        test = self.methods[str(user_input)]()                
                    
    def validate_option(self, user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print "Enter a valid value"            
            
        if 0 < user_input <= len(self.options):            
            return True
        else:
            return False
        
    def manage_users(self):
        print "Create a user"
        
    def manage_customers(self):
        print "Create a customer"
        
    def manage_movies(self):
        print "Create a movie"
        
    def manage_operations(self):
        print "Create an operation"
