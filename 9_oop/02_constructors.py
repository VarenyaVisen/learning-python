class Employee: 

    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond

# self : It refers to the instance of the object calling the method
#self is a convention used as the first parameter in instance methods within a class
# self is basically a reference to a object of a class which is being created
    def get_salary(self):
        return self.salary # a self is important here because self is a way to reference the object
        # of the class which is being created

    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")
    

e1 = Employee(34000, "John Doe", 4)
# print(e1.get_salary())
e1.get_info()