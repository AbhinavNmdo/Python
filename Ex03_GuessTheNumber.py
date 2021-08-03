n = 24
print("Guess The Number")
noofguess = 1

while noofguess<=9:
    i = int(input())
    if i < n:
         print("Up your value, Try again")
         noofguess = noofguess + 1
    elif i > n:
        print("Down your value, Try again")
        noofguess = noofguess + 1
    elif i==n:
        print("Yes, you got it")
        break

if noofguess == 10:
    print("Game Over")
else:
    print("You guess the number in ", noofguess , " attempts")