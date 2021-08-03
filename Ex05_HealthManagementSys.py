print("1 for Ashu \n2 for PapaJi \n3 for MummyJi")
choose = int(input())
if choose == 1:
    print("1 for Exercise \n2 for Food")
    choose2 = int(input())
    if choose2 == 1:
        print("Enter Exercise name to submit in the file")
        exname = input()
        with open("AshuEx.txt", "a")as f:
            f = f.write(exname + "\n")
            print("Success")

    elif choose2 == 2:
        print("Enter Food name to submit in the file")
        foodname = input()
        with open("AshuFo.txt", "a")as d:
            d = d.write(foodname + "\n")
            print("Success")

    else:
        print("Enter valid input like \n1 for Exercise \n2 for Food")

elif choose == 2:
    print("1 for Exercise \n2 for Food")
    choose2 = int(input())
    if choose2 == 1:
        print("Enter Exercise name to submit in the file")
        exname = input()
        with open("PapaJiEx.txt", "a")as f:
            f = f.write(exname + "\n")
            print("Success")

    elif choose2 == 2:
        print("Enter Food name to submit in the file")
        foodname = input()
        with open("PapaJiFo.txt", "a")as d:
            d = d.write(foodname + "\n")
            print("Success")

    else:
        print("Enter valid input like \n1 for Exercise \n2 for Food")

elif choose == 3:
    print("1 for Exercise \n2 for Food")
    choose2 = int(input())
    if choose2 == 1:
        print("Enter Exercise name to submit in the file")
        exname = input()
        with open("MummyJiEx.txt", "a")as f:
            f = f.write(exname + "\n")
            print("Success")

    elif choose2 == 2:
        print("Enter Food name to submit in the file")
        foodname = input()
        with open("MummyJiFo.txt", "a")as d:
            d = d.write(foodname + "\n")
            print("Success")

    else:
        print("Enter valid input like \n1 for Exercise \n2 for Food")

else:
    print("Enter valid Input")
