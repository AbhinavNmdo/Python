class Employees():
    def __init__(self, aname, asalery, arole):
        self.name = aname
        self.salery = asalery
        self.role = arole

    def printdetails(self):
        return f"My name is {self.name}, and my salery is {self.salery} and my role is {self.role}"

abhay = Employees("Abhay", 45454545, "Programmer")

print(abhay.printdetails())