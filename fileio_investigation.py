# fileio_investigation.py


f = open("test.txt", "r")
lines = f.readlines()
print (lines)
f.close()

print ("*" * 40)
print ("second method")

f = open("test.txt", "r")
# note - things in python are quite consistent
# anything that has a list is probably iterable
for line in f:
    print (line, end="")

f.close()

# we can use "with" to automatically close the file
with open("test.txt", "r") as f:
    for line in f:
        print (line, end="")
    
# the file will be automatically closed here


print ("*" * 40)

names = ["Alice", "Bob", "Carol", "Dan", "Eve", "Fred", "Ger", "Harriet", "Ingrid", "John"]

with open ("names.txt", "w") as f:
    for name in names:
        f.write(f"{name}\n")
    










