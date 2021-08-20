import json
data = '{"Name": "Abhay", "role": "Programmer", "isbad": "False"}'
# print(data)     # Returns the dictionary as same as i input
parsed = json.loads(data)
print(parsed)       # Returns the json compatible dictionary
print(parsed['Name'])

# parsed2 = json.load(parsed)       # This command will decode the json file to the python readable
data2 = {
    "Name": "Ashu",
    "Role": "CA",
    "isbad": False
}
a = json.dumps(data2)
print(a)