def is_palindrome(n):
    return str(n) == str(n)[::-1]


def next_palindrome(n):
    if n<10:
        return n
    else:
        n = n + 1
        while not is_palindrome(n):
            n += 1
        return n

if __name__ == '__main__':
    lis = []
    print("Enter the value of cases")
    user = int(input())
    for i in range(user):
        print("Enter the number")
        num = int(input())
        lis.append(num)
    new_lis = []
    for i in range(user):
        n = next_palindrome(lis[i])
        new_lis.append(n)

    print(f"You enter {lis} and their palindrome is {new_lis}")