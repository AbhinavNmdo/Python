print("Enter your value")
Input = int(input())
print("Input 1 or 0")
b = bool(int(input()))

if b == 1:
    for a in range(1, Input + 1):
        print("*" * a)

elif b == 0:
    for d in range(Input, 0, -1):
        print("*" * d)