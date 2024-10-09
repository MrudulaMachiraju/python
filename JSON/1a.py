'''JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.Parse JSON - Convert from JSON to Python
If you have a JSON string, you can parse it by using the json.loads() method.'''
#convert json to Python
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])