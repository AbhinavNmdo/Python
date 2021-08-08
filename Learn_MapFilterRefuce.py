# -------------------MAP----------------------
lis = ["45", "78", "54", "32"]
for i in range(len(lis)):
    lis[i] = int(lis[i])
print(lis[2])

# OR Map Method

psquare = list(map(lambda x: x * x, lis))  # First : Function / Second : list, tuple, dict, etc
print(psquare)


def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]

for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

# ------------FILTER----------------
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def greaterthan5(num):
    return num > 5


greathertahn = list(filter(greaterthan5, list_1))
print(greathertahn)

# --------------REDUCE----------------------
from functools import reduce
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = reduce(lambda a,b:a+b, list_1)
print(a)
