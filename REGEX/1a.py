import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

  '''The findall() Function
The findall() function returns a list containing all matches.'''
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)