#uppercase
x='helloworld'
print(x.upper())
#lower case
z='HEPPOIL'
print(z.lower())
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:


a = " Hello, World! "
print(a.strip())

#replace string
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#split string
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) 