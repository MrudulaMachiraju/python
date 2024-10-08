mytuple = ("rinku", "nani", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#Even strings are iterable objects, and can return an iterator:
mystr = "mrudula"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#looping through iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  #iterate character of the string
  mystr = "banana"
for x in mystr:
  print(x)