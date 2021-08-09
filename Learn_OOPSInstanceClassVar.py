class Students:
    No_of_leaves = 8
    pass

abhay = Students()
ashu = Students()

abhay.name = "Abhay"
abhay.std = "College"
abhay.sub = "Commerce, Maths"

ashu.name = "Ashu"
ashu.std = "CA"
ashu.No_of_leaves = 10
ashu.sub = "Commerce"

print(abhay.No_of_leaves)
print(ashu.No_of_leaves)
print(Students.__dict__)
print(abhay.__dict__)
print(ashu.__dict__)
