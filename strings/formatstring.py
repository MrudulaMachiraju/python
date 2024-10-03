#we cannot combine strings and numbers 
'''To specify a string as an f-string, simply put an f in front of the string literal,
 and add curly brackets {} as placeholders for variables and other operations.'''


age = 36
txt = f"My name is John, I am {age}"
print(txt)

age=29
txt=f"my {age} when i m having kids"
print(txt)
#place holders and modifiers
price=88
txt=f"the price of the tango is {price}"
print(txt)
#display price with two decimals
price=88
txt=f"the price of the tango is {price:.2f}"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)