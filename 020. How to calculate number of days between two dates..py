# How to calculate number days between two dates.
from datetime import date

first_date = date(2020, 6, 11)
second_date = date(1995, 3, 12)

diff = first_date - second_date

print(f"{diff.days} Days")
