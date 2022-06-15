# How to get a new string from a given string

def new_string(s):
    if len(s) >= 2 and s[:2] == "is":
        return s
    return "is " + s

print(new_string("Edward"))
print(new_string("isHE"))