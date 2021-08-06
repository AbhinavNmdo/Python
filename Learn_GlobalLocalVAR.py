x = 1000  # Global Variable
def function():
    x = 2000   # Local Variable
    print("Hello!")



def abhay():
    c = 70000
    def ashu():
        global c
        c = 60000
        print(c)
    print("Before Ashu")
    ashu()
    print("After Ashu")

abhay()

