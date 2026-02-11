import unittest
from employee import Employee

class EmployeeTestCases(unittest.TestCase):
    """test case for employees information"""
    def setUp(self):
            """set up to re-use for every test"""
            self.my_employee = Employee("jhon",'smith',"1000")
    
    
    def test_employees(self):
        """testing if employee information is processed correctly"""
        information = self.my_employee.info()
        self.assertEqual("Jhon Smith Salary : 1000", information)

    def test_give_default_raise(self):
        """unitest to check if the default raise works correctly"""
        self.my_employee.raise_salary()
        salary = self.my_employee.salary
        self.assertEqual(6000, salary)
    def test_give_custom_raise(self):
        """unitest to check if the customized raise works correctly"""
        self.my_employee.raise_salary(7000)
        salary = self.my_employee.salary
        self.assertEqual(8000, salary)

unittest.main()