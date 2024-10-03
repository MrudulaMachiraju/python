thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#change range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#insertion
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)