import json

str = '''
[{
    "name": "wwwww",
    "age": "100"
},{
    "name": "fffff",
    "age": "235"
}]
'''

print(type(str))

data = json.loads(str)
print(data)
print(type(data))

json_str = json.dumps(data)
print(json_str)
print(type(json_str))