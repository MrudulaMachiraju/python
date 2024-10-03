#Create a variable outside of a function, and use it inside the function
x=' awesome'

def myfunc():
  print('i am always' + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x=' awesome'
def myfunc():
  x='fantastic'
  print('i am always' + x)
myfunc()
print('we are' + x)

#creating global variable inside function

def myfunc():
  global y
  y ='fantastic'

myfunc()
print('i am always' + y)

#Also, use the global keyword if you want to change a global variable inside a function.

z='awesome'
def myfunc():
  global z
  z='fantastic'
myfunc()
print('you are'+z)


