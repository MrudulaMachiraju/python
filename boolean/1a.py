a=9
b=7
if (a>b):
  print(' true')
else:
  print('false')

print(10 > 9)
print(10 == 9)
print(10 < 9)
#evaluate string ndnum
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
'''Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

'''
#some values r false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
print(bool([]))
bool({})


#You can create functions that returns a Boolean Value:
'''def myFunction() :
  return True

print(myFunction())'''
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  '''Python also has many built-in functions that return a boolean value, like the isinstance()
   function, which can be used to determine if an object is of a certain data type:'''
x = 200
print(isinstance(x, int))