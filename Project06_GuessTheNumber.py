import random
bothrnd = []
rnd1 = random.randint(1, 20)
bothrnd.append(rnd1)
rnd2 = random.randint(1, 20)
bothrnd.append(rnd2)

bothturn = []
turn1 = 0
bothturn.append(turn1)
turn2 = 0
bothturn.append(turn2)

name = []
player1 = input("Enter Player 1 name\n")
name.append(player1)
player2 = input("Enter Player 2 name\n")
name.append(player2)

print("Your need to guess the number between 1 and 20 and if you guess it in min number of times then opponents so you win\n")

for i in range(2):
    print(f"{name[i]}'s turn")
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


if bothturn[0] > bothturn[1]:
    print(f"{name[0]} wins the match")
elif bothturn[0] < bothturn[1]:
    print(f"{name[1]} wins the match")
else:
    print("Tie")


