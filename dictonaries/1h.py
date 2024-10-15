import json

# Create a python dict
python_dict = [
        {
            "name" : "John",
            "place" : "Melbourne",
            "age" : 40,
            "gender" : "male"
        },
        {
           "name" : "Smith",
            "place" : "Sydney",
            "age" : 49,
            "gender" : "male" 
        }
]

#Convert the dict into json string

json_string = json.dumps(python_dict)

print(json_string)
