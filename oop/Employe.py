# class Employe:

#     def __init__(self, id, name, address, department, salary):
#         self.id = id
#         self.name = name
#         self.address = address
#         self.department = department
#         self.salary = salary

#     def display(self):
#         displays = ("ID:%d \nName:%s \nAddress:%s \nDepartment:%s \nSalary:%s" %
#                     (self.id, self.name, self.address, self.department, self.salary))
#         return displays


# emp = Employe(101, "Ram", "Baneshwore", "Developer", "40000")
# print(emp.display())

class Employe:
    __id = None
    __name = None
    __address = None
    __department = None
    __salary = None

    def __init__(self, id=None, name=None, address=None, department=None, salary=None):
        if id and name and address and department and salary is None:
            self.__id = 20
            self.__name = "hari"
            self.__address = "lazimpat"
            self.__department = "sales"
            self.__salary = "25000"
        else:
            self.__id = id
            self.__name = name
            self.__address = address
            self.__department = department
            self.__salary = salary

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        displays = ("ID:%d \nName:%s \nAddress:%s \nDepartment:%s \nSalary:%s" %
                    (self.__id, self.__name, self.__address, self.__department, self.__salary))
        return displays


emp = Employe(101, "Ram", "Baneshwore", "Developer", "40000")
print(emp.display())

print()

emp.set_id(100)
print(emp.get_id())

emp.set_name("Akshita")
print(emp.get_name())

emp.set_address("Balaju")
print(emp.get_address())

emp.set_department("Marketing")
print(emp.get_department())

emp.set_salary("100000")
print(emp.get_salary())
