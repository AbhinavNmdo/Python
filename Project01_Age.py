age = int(input("Enter your age or year of birth\n"))
age2 = 100
if 0<age< 150:
    print("You enter your age")
    for i in range(101):
        j = i - age
    print(f"Your age reach to 100 after {j} years approx in {2021 + j} year")

elif 1900<age<2021:
    print("You enter your year of birth")
    print(f"Your age reach to 100 approx in {age + 100} year, after {(age+100)-2021} years")

elif 150<age<1900:
    print("Seems like that you are the oldest person or you kidding with this programm")

elif age>2021:
    print("You are not born yet")

elif age<0:
    print("Please enter positive value")

else:
    print("Something is wrong")