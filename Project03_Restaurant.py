food = []
for i in range(3) :
    inp = input("Enter the Food Name\n")
    if inp == "exit":
        exit()
    else:
        food.append(inp)
print(food)
