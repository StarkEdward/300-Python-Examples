# How to access environment variable in python

import os

path = os.environ["PATH"].split(";")

for i in path:
    print(i)