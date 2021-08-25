import random
rnd = random.randint(1, 20)
print(rnd)
print("Your need to guess the number between 1 and 20 and if you guess it in min number of times then opponents so you win")

for i in range(1):
    print(f"Player {i+1} turn")
    while True:
        user = int(input("Enter your guess\n"))
        if user > rnd:
            print("You Guess bigger number, try agian")
        elif user < rnd:
            print("You Guess smaller number, try again")
        elif user == rnd:
            print("Yes, you guess correct")