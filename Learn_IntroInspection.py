import inspect
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"Email is not set, please set it by using the email setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("Setting now..........")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


abhay = Employee("Abhinav", "Nmadeo")

print(abhay.email)
del abhay.email
print(abhay.email)
print(abhay.fname)
abhay.email = "abhay.namdeo@gmail.com"
print(abhay.email)
