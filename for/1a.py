names = ["tharun", "rinku", "cherry"]
for x in names:
  print(x)
  if x== 'tharun':
    break
'''for x in "tharun":
   print(x)'''


names = ["tharun", "rinku", "cherry"]
for x in names:
  print(x)
  if x== 'tharun':
    continue

  #else in for loop
for x in range(6):
   print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

    #pass
for x in [0, 1, 2]:
  pass