class AccessModifires():
    no_of_leaves = 8
    _protec = "This is protected thing"        # Protected Access Modifire
    __pri = "This is private thing"

    def __init__(self, name, game):
        self.name = name
        self.game = game


abhay = AccessModifires("Abhay", "Basketball")
print(abhay._protec)        # This is How we print the protected Access Modifires
print(abhay._AccessModifires__pri)      # This is How we print private Access Modifires