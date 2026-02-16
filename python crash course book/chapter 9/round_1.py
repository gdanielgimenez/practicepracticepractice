# 9.1 Restaurant
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


# restaurant instance
sushi_place = Restaurant("Tokyo Drift", "sushi")
print(sushi_place.restaurant_name)
print(sushi_place.cuisine_type)
print()
sushi_place.describe_restaurant()
sushi_place.open_restaurant()

# 9.2 Three Restaurants
stake_place = Restaurant("King of the Stakes", "Barbeque")
stake_place.describe_restaurant()
mcdonals = Restaurant("Mcdonald's", "Fast Food")
mcdonals.describe_restaurant()
italian_place = Restaurant("Luigi's", "Italian food")
italian_place.describe_restaurant()

# 9.3 Users


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


# creating instances for the class
batman = User("bruce", "wayne", "thebman@gmail.com", 40, "Gotham City")
batman.user_info()
batman.greet_user()
liam = User("liam", "gallagher", "lg2007@hotmail.com", 50, "Manchester")
liam.user_info()
liam.greet_user()
