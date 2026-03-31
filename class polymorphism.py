class Employee:
    def __init__(self, empid=None, sal=None, dept=None):
        self.empid = empid
        self.sal = sal
        self.dept = dept

    # Method with optional parameters (overloading style)
    def employee_details(self, empid=None, sal=None, dept=None):

        if empid is not None:
            print("Employee ID:", empid)
        else:
            print("Employee ID: missing")

        if sal is not None:
            print("Employee Salary:", sal)
        else:
            print("Employee Salary: missing")

        if dept is not None:
            print("Employee Department:", dept)
        else:
            print("Employee Department: missing")

        print("----------------------")


# Creating object
g1 = Employee()

# Calling method in different ways (overloading style)
g1.employee_details(empid=1008, sal=1009)
g1.employee_details(sal=2500.54)
g1.employee_details(dept="civil")

    
    
