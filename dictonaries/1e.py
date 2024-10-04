mydict={
  'name': 'tharun',
  'age': 28,
  'city': 'melbourne',
  'work': 'wise'
}
#print keys
for x in mydict:
  print(x)
  #print values
for x in mydict:
  print(mydict[x])
#print both
for x, y in mydict.items():
  print(x, y)