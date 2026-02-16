# excercises with class inheritance
# 9-6 ice cream stand => inherits from
# 9.1 Restaurant as a base to start
class Restaurant():
    """class to build a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"Restaurant : {self.restaurant_name} is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"We are open from Noon to 10pm.")


class Ice_cream_stand(Restaurant):
    """modelling ice cream stand from the restauran class"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Available flavors for your iceCream : ")
        for flavor in self.flavors:
            print(f"\t{flavor}")


# begin class instance
chinatown = Ice_cream_stand("chinatown", "icecreams", [
                            'vanilla', 'chocolate', 'americana'])
chinatown.display_flavors()


# 9-7 administrator => create a child class from 9.3
# 9-3 User
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


class Administrator(User):
    """attemp to model an administrator priviledges"""

    def __init__(self, first_name, last_name, email, age, location, privileges):
        super().__init__(first_name, last_name, email, age, location)
        self.privileges = privileges

    def show_privileges(self):
        print("List of admin privileges : ")
        for privilege in self.privileges:
            print(f"\t{privilege}")


# class instance for an administrator
batman = Administrator("bruce", "wayne", "bman@gmail.com", 45, "gotham city",
                       ["ban users", "create users", "create posts", "delete posts"])
batman.show_privileges()

# 9.9 Battery upgrade => from final version of car.py
