class Employee:

    num_of_emps = 0                  # this is a CLASS variable, and defines the variable for the whole class
    min_wage = 10.5
    pay = 0
    raise_percentage = 1.05

    def __init__(self, first, last, position):          # this is a SELF method, and must take "self" as the first argument
        self.first = first           # this is an INSTANCE variable, as it changes for each instance of the class 
        self.last = last
        self.position = position
        self.email = first.lower() + '.' + last.lower() + '@company.co.uk'

        Employee.num_of_emps += 1


    def wage(self):
        if self.position == "FOH":
            self.pay = Employee.min_wage
            return self.pay
        elif self.position == "Supervisor":
            self.pay = Employee.min_wage * 1.05
            return self.pay
        elif self.position == "Manager":
            self.pay = Employee.min_wage * 1.1
            return self.pay

    @classmethod
    def from_string(cls, emp_str):              # this is a CLASS method, and must take "cls" as the first argument
        first, last, position = emp_str.replace("/", "-").split("-")   # if input string uses "/", it is replaced by "-", then split at "-"
        return cls(first, last, position)

    @staticmethod                               # this is a STATIC method, and does not take a "self" or "cls" argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("Lucas", "Pavlou", "FOH")
print(emp_1.first, emp_1.min_wage, emp_1.wage())

emp_2 = Employee.from_string("Joe-Smith-Manager")
print(emp_2.first, emp_2.min_wage, emp_2.wage())

emp_3 = Employee.from_string("Sarah/Connor/Supervisor")
print(emp_3.first, emp_3.min_wage, emp_3.wage())

import datetime
my_date = datetime.date(2023, 10, 7)

print(Employee.is_workday(my_date))
