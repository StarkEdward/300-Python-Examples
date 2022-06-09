# 009. How to Print Current Date and Time in Python
from datetime import datetime

now = datetime.now()
print("Current date and time is:")
print(now.strftime("%y-%m-%d %H:%M:%S"))