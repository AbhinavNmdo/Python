class Abhay():
    var1 = "I am variable in class abhay var1"
    def __init__(self):
        self.var1 = "I am var1 now I am inside on the init function of class A"
        self.special = "I am Special variable on the A's init function"

class Ashu(Abhay):
    var1 = "I am var1 now I am in the class ashu"
    def __init__(self):
        self.var1 = "I am var1 now I am inside the init init function of the class B"
        super(Ashu, self).__init__()

a = Abhay()
b = Ashu()
print(b.special)
