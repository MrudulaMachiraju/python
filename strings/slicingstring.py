'''You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

'''
#Get the characters from position 2 to position 5 (not included):
b="Hello, world!"
print(b[2:5])
#slice from the start
#Get the characters from the start to position 5 (not included):
print(b[:5])
#slice to the end
#Get the characters from position 2, and all the way to the end:
print(b[2:])
#negative indexing
#Use negative indexes to start the slice from the end of the string:
'''Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):'''
print(b[-5:-2])