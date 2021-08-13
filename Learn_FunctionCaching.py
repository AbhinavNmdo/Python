import time
from functools import lru_cache

@lru_cache(maxsize=3)
def time_taken(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Work is Starting...")
    time_taken(3)
    print("Again Work is Starting....")
    time_taken(3)
    print("Again and Again Work is Starting.....")
