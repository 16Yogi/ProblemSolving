# def fun1():
#     import json

#     json1 = '{"name":"Ramlal","age":30,"add":"Bhopal"}'
#     res1 = json.loads(json1)
#     print(res1["name"])
#     print(res1["age"])

# fun1()

# json1 = 'https://jsonplaceholder.typicode.com/todos/1'
# print(json1)


import json

json1 = {
    "name":"Ramlal",
    "age":50,
    "add":"Kerla"
}
json2 = x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

res1 = json.dumps(json1)
res2 = json.dumps(json2)
print(res1)
print(res2)