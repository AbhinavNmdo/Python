def names(n, friends):
    for i in range(n):
        name = input(f"Enter the name of {i} friend")
        friends.append(name)

def jumbelName(friends):
    name = friends.split(" ")
