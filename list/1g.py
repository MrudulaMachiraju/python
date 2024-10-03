'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
#condition
#The condition is like a filter that only accepts the items that valuate to True.
newlist = [x for x in fruits if x != "apple"]
#iterable
#The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]