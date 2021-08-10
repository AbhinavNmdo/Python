class Employees():
    def __init__(self, name, role, number):
        self.name = name
        self.role = role
        self.number = number

    def printdetails(self):
        return f"My name is {self.name}, and my role is {self.role}, and my number is {self.number}"

class Player():
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetailofplayer(self):
        return f"My name is {self.name}, and I am perfect on {self.game} game"

# class CoolProgrammer(Employees, Player):
#     pass
# abhay = CoolProgrammer("Abhay", "Programmer", "7878788787")
# print(abhay.printdetails())

class CoolProgrammer(Player, Employees):
    launguage = "Java, Python, HTML, CSS, JavaScript"
    def printlanguage(self):
        print(self.launguage)
abhay = CoolProgrammer("Abhay", "Basketball")
print(abhay.printdetailofplayer())
print(abhay.printlanguage())