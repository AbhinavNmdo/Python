class A():
    def met(self):
        print("I am the function inside the class A")
    # pass

class B(A):
    def met(self):
        print("I am the function inside the class B")
    # pass

class C(A):
    def met(self):
        print("I am the function inside the class C")
    # pass

class D(B, C):
    pass


a = A()
b = B()
c = C()
d = D()

print(b.met())
print(d.met())