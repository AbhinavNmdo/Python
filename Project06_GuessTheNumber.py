import random


def player(n, list):
    for i in range(int(n)):
        e = input("Enter Player name\n")
        list.append(e)


def turn(n, list):
    for i in range(int(n)):
        a = 0
        list.append(a)


def rand(n, list):
    for i in range(int(n)):
        rnd = random.randint(1, 20)
        list.append(rnd)


def winner(n):
    large = min(bothturn)
    index = bothturn.index(large)
    print(f"Player\t\t\tTurns")
    for i in range(n):
        print(f"{name[i]}\t\t\t{bothturn[i]}")
    print(f"Winner is {name[index]}")


game = int(input("Enter the no of Players\n"))
name = []
bothrnd = []
bothturn = []
player(game, name)
rand(game, bothrnd)
turn(game, bothturn)

print(
    "Your need to guess the number between 1 and 20 and if you guess it in min number of times then opponents so you win\n")

for i in range(game):
    print(f"{name[i]}'s turn")
    print(bothrnd[i])
    while True:
        try:
            user = int(input("Enter your guess\n"))
            if user > 20 or user < 0:
                print("Please Enter valid number")

            else:
                if user > bothrnd[i]:
                    print("Greater, try again")
                    bothturn[i] += 1
                    print("----------------------------------------------------\n")
                elif user < bothrnd[i]:
                    print("Smaller, try again")
                    bothturn[i] += 1
                    print("----------------------------------------------------\n")
                elif user == bothrnd[i]:
                    bothturn[i] += 1
                    print(f"You guess the right number in {bothturn[i]} turns")
                    print("----------------------------------------------------\n")
                    break
        except:
            print("Something is wrong")

print("---------------------------")
winner(game)
print("---------------------------")
