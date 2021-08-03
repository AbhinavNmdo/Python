import plistlib

print("\n\n\n\n\t\t\t\t\t\t\t\t\t\tWelcome to SizerPaperRock Game")
print("---------------------------------------------------------------------------------------------------------------")
print("Note: ")
print("If you got 5 win before then the computer then you win, other wise computer win")
print("---------------------------------------------------------------")
import random

lst = ["Sizer", "Paper", "Rock"]
print("Choose:\n1. for Sizer\n2. for Paper\n3. for Rock")
s = "Sizer"
p = "Paper"
r = "Rock"
compWins = 0
yourWins = 0

while compWins < 5 and yourWins < 5:
    comp = random.choice(lst)
    print(comp)
    if comp == "Sizer":
        you = int(input())
        if you == 1:
            print(f"You Choose, {s}")
            print("Winner,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 2:
            compWins = compWins + 1
            print(f"You Choose, {p}")
            print("Winner,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 3:
            yourWins = yourWins + 1
            print(f"You Choose, {r}")
            print("Winner,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")


    elif comp == "Paper":
        you = int(input())
        if you == 1:
            yourWins = yourWins + 1
            print(f"You Choose, {s}")
            print("Winner,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 2:
            print(f"You Choose, {p}")
            print("Tie,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 3:
            compWins = compWins + 1
            print(f"You Choose, {r}")
            print("Loser,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")

    elif comp == "Rock":
        you = int(input())
        if you == 1:
            compWins = compWins + 1
            print(f"You Choose, {s}")
            print("Loser,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 2:
            yourWins = yourWins + 1
            print(f"You Choose, {p}")
            print("Winner,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")
        elif you == 3:
            print(f"You Choose, {r}")
            print("Tie,\nYour Score: ", yourWins, "\nComputer Score: ", compWins)
            print("---------------------------------------------------------------")

if compWins == 5:
    print("Game over")
elif yourWins == 5:
    print("You won the whole game")
