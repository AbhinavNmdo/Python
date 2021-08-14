
try:
    f1 = open("LibraryLog.txt")
    # f2 = open("asdf.txt")

except Exception as e:
    print(e)

# If except is run then the else statement not run or vice versa
else:
    print("This is Else Statement")

# finally Statement always running in any condition
finally:
    print("This is finally statement")