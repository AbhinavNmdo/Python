class Employees():
    no_of_leaves = 8

    def __init__(self, aname, asalery, arole):
        self.name = aname
        self.salery = asalery
        self.role = arole

    def printdetails(self):
        return f"My name is {self.name}, and my salery is {self.salery} and my role is {self.role}"

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves


abhay = Employees("Abhay", 45454545, "Programmer")
ashu = Employees("Ashu", 45454544, "CA")
papaji = Employees("Abhishek / 455445454 / WebDeveloper")
abhay.change_leaves(20)

print(ashu.no_of_leaves)
print(abhay.no_of_leaves)