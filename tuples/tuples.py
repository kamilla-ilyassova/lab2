thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #with duplicates

tuple1 = ("abc", 34, True, 40, "male") #with different data types

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) #length
print(type(thistuple)) #type

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

