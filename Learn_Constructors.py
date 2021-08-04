class Employees:
    def __init__(self, aname, asalery, anumber):
        self.name = aname
        self.salery = asalery
        self.number = anumber

    def printdetails(self):
        return f"My name is {self.name} and my number is {self.number} and my salery is {self.salery}"


abhay = Employees("Abhay", 787878, 7823564656)
ashu = Employees("Ashu", 784545, 7878654654)

print(ashu.printdetails())
print(abhay.printdetails())