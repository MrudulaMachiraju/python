import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
'''The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:'''
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))