#global scope -  A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#Global variables are available from within any scope, global and local.
'''x = 300

def myfunc():
  print(x)

myfunc()

print(x)'''
#naming variable
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

'''x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)'''
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#The global keyword makes the variable global.

'''def myfunc():
  global x
  x = 300

myfunc()

print(x)'''

#The nonlocal keyword is used to work with variables inside nested functions.
#The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())