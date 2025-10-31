# enumerate_investigation.py

result = [('-l', ''), ('-w', ''), ('-c', '')]


# you can extract the element from a tuple as you are iterating 
# through them

# use _ if you aren't going to use a particular value

# round brackets are option (sometimes)
for (option, _) in result:
    print (option)


t = (1,2,3)

(a, b, c) = t

print (a)
print (b)
print (c)

# round brackets are optional here
a,b,c = t

print (a)
print (b)
print (c)

options = []
for option, _ in result:
    print (option)
    options.append(option)

print (options)    


# to do this in the proper pythonic way


options = [option for option, _ in result]

print (options)



# enumerating a list


names = ["Alice", "Bob", "Carol", "Dan"]

# 1 Alice
# 2 Bob
# 3 Carol
# 4 Dan

for i in range (len(names)):
    print (f"{i+1} {names[i]}")

# but this isn't very pythonic

count = 1
for name in names:
    print (f"{count} {name}")
    count += 1

# this isn't very pythonic either

for item in enumerate(names):
    print (f"{item[0]+1} {item[1]}")

# not quite optimal

# this is the optimal solution:
for index, name in enumerate(names):
    print (f"{index+1} {name}")










