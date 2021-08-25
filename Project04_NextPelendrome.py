def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n += 1
    return n

if __name__ == '__main__':
    lis = []
    print("Enter the Number of cases you want")
    user = int(input())
    for i in range(user):
        num = int(input("Enter the Number\n"))
        lis.append(num)

    for i in range(user):
        print(f"Your next Palindrome of {lis[i]} is {next_palindrome(lis[i])}")