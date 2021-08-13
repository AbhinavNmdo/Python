# Short method
dict1 = {i for i in range (40) if i%2==0}
print(dict1)
dict2 = {k:f"Item {k}" for k in range(11)}
print(dict2)
dict3 = {d:f"Item {d}" for d in range(11)}
dict3 = {value:key for key, value in dict3.items()}
print(dict3)