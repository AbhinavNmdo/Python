# All function are given in this website (https://documentation.help/Python-PEP/operator-map.html)
class Employees():
    no_of_leaves = 8

    def __init__(self, aname, asalery, arole):
        self.name = aname
        self.salery = asalery
        self.role = arole

    def printdetails(self):
        return f"My name is {self.name}, and my salery is {self.salery} and my role is {self.role}"

    def __add__(self, other):
        return self.salery + other.salery

    def __repr__(self):
        return f"Employee {self.name}, salery {self.salery}, role {self.role}"

    # def __str__(self):
    #     return f"String {self.name}, {self.salery}, {self.role}"

abhay = Employees("Abhay", 455, "Programmer")
ashu = Employees("Ashu", 455, "CA")

print(abhay + ashu)
print(abhay)