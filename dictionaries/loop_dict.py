thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#KEYS
for x in thisdict:
  print(x)
for x in thisdict.keys():
  print(x)
#VALUES
for x in thisdict:
  print(thisdict[x])
for x in thisdict.values():
  print(x)
#BOTH KEYS AND VALUES
for x, y in thisdict.items():
  print(x, y)
