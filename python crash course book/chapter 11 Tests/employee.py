class Employee():
    """stores information about employees"""


    def __init__(self,first_name,last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
    
    def info(self):
        employee_info = f"{self.first_name.title()} {self.last_name.title()} Salary : {str(self.salary)}"
        print(f"{self.first_name.title()} {self.last_name.title()} Salary : {str(self.salary)}")
        return employee_info
    def raise_salary(self, amount="5000"):
        if amount:
            self.salary+= int(amount)
        else:
            self.salary+= int(5000)

        

