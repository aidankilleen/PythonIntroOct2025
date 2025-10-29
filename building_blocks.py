# building_blocks.py
#
# all programming languages use the same core building blocks


# building block #1 - comment

print ("Buiding Blocks") # you can put a comment at the end of a line

"""
You can have multi-line comments using 3 quotation marks

"""
# print the word "welcome" 
# only comment when you are adding some value - don't just state the obvious
print ("welcome")


# building block #2 - variables

name = "Aidan"
cost = 10
rate = 1.23
active = True

print ("Welcome " )
print (name)

name = "Mary"
print ("Welcome")
print (name)

# "pythonic" - things that are unique to python
value = 10

value = "ten" # in python variables are not strongly typed - i.e. you can change the type

# python can work with really large numbers - most languages can't
value = 2342342389947283749234972349723497823974329724397234

print (value * 10)


# building block #3 - expression

value = 10

answer = value * 3.14

name = "Aidan"

message = "Welcome " + name

print (message)

answer = value * 10 / 50 ** 2 + 45 - 12

print (answer)

# there is a defined order of operations
# P - parenthesis
# E - exponents
# M - multiplication
# D - division
# A - addition
# S - subtraction

# recommend using parenthesis
answer = ((value * 10) / (50 ** 2)) + (45 - 12)

# pythonic expressions:
# you can multiply a string in python
print ("*" * 50)


# building block #4 - looping

count = 1

while count <= 10:
    print (count)
    count = count + 1

print ("finished")

# for loop
total = 0
for i in range(100000):
    total = total + i

print ("The total is ")
print (total)

print ("The total is " + str(total))


#  pythonic note - python is a very performant language

# bulding block # 5 - condition - if statement
for n in range (10):
    if n == 5:
        print ("five")
    elif n == 7:
        print ("*" * 7)
    else:
        print (n)

# pythonic - inline condition
n = 5

if n > 5:
    print ("The value is big")
else:
    print ("The value is small")

# use an if in the middle of an expression
n = 5
message = "The value is " + ("big" if n > 5 else "small")

print (message)


# bulding block #6 - list (arrays in other programming languages)
names = ["Alice", "Bob", "Carol", "Dan", "Eve"]

print (names[1]) # index starts at 0
print (names[0]) # this is the first element in the list

print (len(names))

# you can loop through a list very easily
for name in names:
    print (name)

print ("*" * 30)
# pythonic feature
print (names[-1]) # return the last item in the list



# building block #7 - functions
print("hello")
val = str(12345)
print ("the answer is " + val)
len(names)

# built in functions
# https://docs.python.org/3/library/functions.html


# user defined functions
def greet(name):
    return "Welcome " + name

print (greet("Aidan"))

# building block #8 - objects
name = "Aidan"

# name is a string which is an object

print (name.upper())


# we will be encountering objects
# we will be using built in objects
# we will be using standard library objects
# we will be using 3rd party objects
# we will be creating our own user-defined objects.





























































































