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
