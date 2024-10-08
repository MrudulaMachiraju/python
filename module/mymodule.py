'''module just save the code you want in a file with the file extension .py:

ExampleGet your own Python Server
Save this code in a file named mymodule.py'''

def greeting(name):
  print("Hello, " + name)
'''Use a Module
Now we can use the module we just created, by using the import statement:

Example
Import the module named mymodule, and call the greeting function:'''
import mymodule
mymodule.greeting("Jonathan")
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)
#Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)