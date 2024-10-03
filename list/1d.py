#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#insertion
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)