# all modules to work with the last round of chapter 9 excercises
class Restaurant():
    """class to build a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(
            f"Restaurant : {self.restaurant_name} is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"We are open from Noon to 10pm.")

    def set_number_served(self, number):
        self.number_served = number
        print(
            f"A total of {self.number_served} customers have been served tonight.")

    def increment_number_served(self, number):
        self.number_served += int(number)


# admin class
# 9-8 Pivileges
class User():
    """modelling users for a web page"""

    def __init__(self, first_name, last_name, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.location = location

    def greet_user(self):
        print(
            f"Welcome to the system {self.first_name.title()} {self.last_name.title()}")

    def user_info(self):
        print(f"User : {self.first_name.title()} {self.last_name.title()}")
        print(f"email : {self.email}")
        print(f"age : {self.age}")
        print(f"location : {self.location}")


class Privileges():
    """manage list of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self, ):
        print("List of admin privileges : ")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Administrator(User):
    """attemp to model an administrator priviledges"""

    def __init__(self, first_name, last_name, email, age, location, privileges):
        super().__init__(first_name, last_name, email, age, location)
        self.privileges = Privileges(privileges)
