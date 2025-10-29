# tuple_investigation.py

people = ("Alice", "Bob", "Carol", "Dan", "Eve", "Fred", "Ger", "Harriet", "Ingrid", "John")

print (people)

print (people[0])
print (people[-1])

print (len(people))

print (people[3:7])
print (people[:3])
print (people[7:])

print (people[::2])
print (people[1::2])

# tuples are immutable - ie. we can't modify
# people[0] = "ALICE"


# uses for tuples

# assign multiple values at once

a =1
b=2
c=3
d=4
# pythonic way to do multiple assignments is to use 
# tuples
(a,b,c,d) = (1, 2, 3, 4)

# swap 2 variables without needing a temporary
a = 1
b = 2

print (f"{a} {b}")
# swap these using the traditional temporary method
t = a
a = b
b = t
print (f"{a} {b}")

# swap using tuple assignment
(a, b) = (b, a)

print (f"{a} {b}")

# return multiple values from a function

























