import time
"""
initial = time.time()
i = 0
for i in range(45):
    print(i)
    i = i + 1
print(f"For loop is end in {time.time() - initial} seconds")

initial2 = time.time()
j = 0
while j < 45:
    print(j)
    j = j + 1
print(f"While loop is is end in {time.time() - initial2} seconds")
"""

# Time Module Functions
print(time.time())
print(time.gmtime(0))
print(time.localtime())
print(time.ctime())
# print("Time Before")
# time.sleep(3)
# print("Time After")
print(time.asctime())
result = time.localtime(1628220222.9788752)
print("Result:    ", result)
print("Year", result.tm_year)
print("Month", result.tm_mon)
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
print(time.mktime(t))
print(time.strftime("%d/%m/%Y"))
print(time.process_time())
print(time.asctime())
