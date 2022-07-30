# How to count the number of items  in a list in python

def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    return count


print(list_count([1, 2, 3, 4, 4, 5]))