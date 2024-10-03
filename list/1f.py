#loop through a list
mylist=["apple", "banana", "cherry"]
for x in mylist:
  print(x)
  #loop through index numbers
  #Use the range() and len() functions to create a suitable iterable.
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  #using while loop
  list = ["apple", "banana", "cherry","curry"]
i = 0
while i < len(list):
  print(list[i])
  i = i + 1
  #loop using list comprehension
  thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]