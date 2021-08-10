class Experties():
    def __init__(self, name, sub, section):
        self.name = name
        self.sub = sub
        self.section = section

    def printde(self):
        return f"My name is {self.name}, and subjects is {self.sub}"


class Programmer(Experties):
    def __init__(self, name, sub, section, language):
        self.language = language
        self.name = name
        self.sub = sub
        self.section = section


    def printdef(self):
        return f"My name is {self.name}, and subjects is {self.sub} and I learned {self.language}"

ashu = Experties("Ashu", "Commerce", "B")
abhay = Programmer("Abhay", "Commerce, Maths", "B", "Java, Python, HTML, CSS, Javascript")

print(ashu.printde())
print(abhay.printdef())
