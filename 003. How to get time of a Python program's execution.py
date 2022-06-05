# 003. How to get time of a Python program's execution

import time


def get_time():
    start_time = time.time()
    s = 0
    for i in range(1, n + 1):
        s = s + i

    end_time = time.time()
    return s, end_time - start_time


n = int(input("Enter number: "))
print(f"Time required for program's execution is: {get_time()}")
