lst = ["Abhay", "Ashu", "PapaJi", "MummyJi"]
i = 1
for item in lst:
    if i % 2 != 0:
        print(f"Hey, I am {item}")
    i += 1

for index, item in enumerate(lst):
    if index % 2 == 0:
        print(f"Hey, I am {item}")