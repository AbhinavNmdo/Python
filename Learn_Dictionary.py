dic = {"Abhay":"Programmer", "Ashu":"CA", "PapaJi":"WebDesigner", "MummyJi":"HouseWife"}

print("-------------------------------------------------------------------------------------")
print(type(dic))
print("-------------------------------------------------------------------------------------")
print(dic)
print("-------------------------------------------------------------------------------------")
print(dic["Abhay"])
print("-------------------------------------------------------------------------------------")
print(dic.keys())
print("-------------------------------------------------------------------------------------")
print(dic.items())
print("-------------------------------------------------------------------------------------")
dic.update({"Mikki":"Parrot"})
# dic["sldkfj"] = "skfdj"
print(dic)
print("-------------------------------------------------------------------------------------")
dic3 = dic.copy()
del dic3["Abhay"]
print(dic)
print(dic3)
print("-------------------------------------------------------------------------------------")
