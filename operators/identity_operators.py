x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)   # returns True because z is the same object as x

print(x is y)   # returns False because x is not the same object as y

print(x == y)   # to demonstrate the difference betweeen "is" and "==": 

print(x is not z)   # returns False because z is the same object as x

print(x is not y)   # returns True because x is not the same object as y

print(x != y)  # to demonstrate the difference betweeen "is not" and "!=": 