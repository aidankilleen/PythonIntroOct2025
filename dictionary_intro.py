# dictionary_intro.py

# a dictionary is a data structure that allows me to store values
# with a key

# curly brackets are used for dictionaries
from datetime import date


d = {
    "name": "Alice", 
    "county": "Dublin", 
    "phone": "087 1239876"
}

print (d)
print (d["name"])

# you can add new items to a dictionary (mutable)
d["country"]  = "Ireland"
print (d)

# print (d["doesntexist"]) # if you access an item that doesn't exist you get KeyError

# you can iterate through a dictionary
for key in d:
    print (f"{key} - {d[key]}")

print (d.keys())
print (d.values())
print (d.items())


d["age"] = 21
d["dob"] = date.fromisoformat("1980-05-01")

# you can have a list in a dictionary
d["qualifications"] = ["Leaving Cert", "BSC", "MSC", "PhD"]

print (d)

for qualification in d["qualifications"]:
    print (qualification)


# you could have a list contains dictionaries

team = [
    {"name":"Alice", "title":"Manager"}, 
    {"name":"Bob", "title":"Intern"}, 
    {"name":"Carol", "title":"Developer"}
]

for item in team:
    print (f"{item["name"]} - {item["title"]}")



















