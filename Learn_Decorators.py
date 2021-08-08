def functoin1(function2):
    def nowexe():
        print("Executing")
        function2()
        print("Executed now")
    return nowexe()


@functoin1
def name():
    print("I am Abhinav")


# name = functoin1(name())
# name()
