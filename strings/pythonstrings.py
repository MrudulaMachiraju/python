#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#strings are arrray
a = "Hello, World!"
print(a[1])
#looping through a string
for x in "banana":
  print(x)
  #string length
a = "Hello, World!"
print(len(a))
#checkstring
txt = "The best things in life are free!"
print("free" in txt)
#use it in if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #checkif not
txt = "The best things in life are free!"
print("expensive" not in txt)