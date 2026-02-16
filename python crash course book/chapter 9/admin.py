# separated from round_3 file cause it requires refactor an existing class
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


# class instance for an administrator new version should work with a minimal change when calling the func
# show privileges, now having to call first the class privilege => admin.privilege.show_privileges()
batman = Administrator("bruce", "wayne", "bman@gmail.com", 45, "gotham city",
                       ["ban users", "create users", "create posts", "delete posts"])
batman.privileges.show_privileges()
