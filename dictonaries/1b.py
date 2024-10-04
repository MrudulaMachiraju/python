thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x = thisdict.get("model")
print(x)
x = thisdict.keys()
print(x)

mydict= {
  'name': 'tharun',
  'age': 28,
  'city': 'melbourne',
  'work': 'wise'
}
x=mydict.values()
print(x)
mydict['nation']='indian'
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")