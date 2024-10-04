
#creating a function
def my_function():
  print("Hello from a function")

#calling a function
def my_function():
  print("Hello from a function")

my_function()
#arguments
def my_function(fname):
  print(fname + " is a programmer")

my_function("rinku")
my_function("tharun")
#no of arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("rinku", "mrudula")
#keyword arguments
def my_function(fname, lname, age):
  print(fname + " " + lname + " is " + str(age) + " years old")

my_function(lname="mrudula", fname="rinku", age=28)

#passing list into an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#return values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(x):
  print(x)

my_function(x = 3)
