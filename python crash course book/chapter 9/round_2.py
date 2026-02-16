# 9-4 Number served =>  start with code from 9.1 restaurant
# 9.1 Restaurant
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


# class instance
sushiland = Restaurant("sushiland", "japanese cuisine", "20")
print(sushiland.number_served)
sushiland.number_served = "35"
print(sushiland.number_served)
sushiland.set_number_served(45)
sushiland.increment_number_served(5)
print(sushiland.number_served)


# 9.5 login attemps => start with 9.3
class User():
    """modelling users for a web page"""

    def __init__(self, first_name, last_name, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.location = location
        self.login_attemps = 0

    def greet_user(self):
        print(
            f"Welcome to the system {self.first_name.title()} {self.last_name.title()}")

    def user_info(self):
        print(f"User : {self.first_name.title()} {self.last_name.title()}")
        print(f"email : {self.email}")
        print(f"age : {self.age}")
        print(f"location : {self.location}")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


# class instance
batman = User("bruce", "wayne", "thebman@gmail.com", 40, "Gotham City")
batman.increment_login_attemps()
batman.increment_login_attemps()
batman.increment_login_attemps()
print(batman.login_attemps)
batman.reset_login_attemps()
print(batman.login_attemps)
