n = int(input("Enter the value of Apples Abhay got\n"))
mn = int(input("Enter the minimum value\n"))
mx = int(input("Enter the maximum value\n"))

if mn==mx:
    print("Do not enter min and max value same")

else:
    for mn in range(mx+1):
        try:
            if n % mn == 0:
                print(f"{mn} is divisor of {n}")
            else:
                print(f"{mn} is not divisor of {n}")
        except:
            print("Something wrong")