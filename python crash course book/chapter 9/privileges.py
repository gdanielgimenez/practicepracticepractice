from user import User


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
