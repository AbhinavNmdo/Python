def name(*args, **kwargs):  # Always follow this ==>  (normal statement, args statement, kwargs statement)
    print("This is args statement")
    for item in args:
        print(item)
    print("This is kwargs statement")
    for i, j in kwargs.items():
        print(f"{i} is a {j}")


names = ["Abhay", "Ashu", "PapaJi", "MummyJi"]  # Add krte jao isme koi error nhi aaiega
print(name(*names))
names2 = {"Abhay": "Programmer", "Ashu": "CA", "PapaJi": "WebDeveloper", "MummyJi": "HouseWife"}
print(name(**names2))
