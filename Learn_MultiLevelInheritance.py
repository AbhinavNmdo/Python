class ElectronicPhone():
    def calling(self):
        return "Calling through Electronic Device"


class PocketPhone(ElectronicPhone):
    def calling(self):
        return "Calling through the Pocket Phone"

    def music(self):
        return "Playing music through the Pocket Phone"


class SmartPhone(PocketPhone):
    def calling(self):
        return "Calling through the Smart Phone"

    def music(self):
        return "Playing music through the Smart Phone"

    def gaming(self):
        return "Playing game"


phone = ElectronicPhone()
phone2 = PocketPhone()
phone3 = SmartPhone()

print(phone.calling())
print(phone2.calling())
print(phone3.calling())

print("----------------------------------------------")

print(phone2.music())
print(phone3.music())

print("----------------------------------------------")

print(phone3.gaming())