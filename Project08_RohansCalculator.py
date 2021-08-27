def rohanCalculator(table):
    for i in range(10):
        multi = 6 * (i+1)
        wrong = (6 * 6) + 2
        table.append(multi)
    table.remove(36)
    table.insert(5, 38)
    return table

def checkRohanCal(table):
    correctTable = []
    for i in range(10):
        multi = 6 * (i+1)
        correctTable.append(multi)
    for j in range(10):
        if table[j] != correctTable[j]:
            print(f"Something is wrong in {table[j]}")

if __name__ == '__main__':
    rohanTabele = []
    rohan = rohanCalculator(rohanTabele)
    print(rohan)
    checkRohanCal(rohan)