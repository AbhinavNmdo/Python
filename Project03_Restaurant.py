food = []
for i in range(5):
    inp = input("Enter the Food Name\n")
    food.append(inp)
print("Reverse by inbuilt python method")
foodwithreverse = food
foodwithreverse.reverse()
print(foodwithreverse)
print("----------------------------------------------------")
print("Reverse by Slicing")
foodwithslicing = food
foodwithslicing[::-1]
print(foodwithslicing)
print("----------------------------------------------------")
print("Reverse by using Swapping method")
foodwithswapping = food
for i in range(len(foodwithswapping)//2):
    foodwithswapping[i], foodwithswapping[len(foodwithswapping) -i -1] = foodwithswapping[len(foodwithswapping) -i -1], foodwithswapping[i]
print(foodwithswapping)
