# list_slicing_investigation.py

people = ["Alice", "Bob", "Carol", "Dan", "Eve", "Fred", "Ger", "Harriet", "Ingrid", "John"]


print (len(people))

print (people[0])
print (people[-1])

# list slicing works exactly the same way as string slicing
print (people[3:7])
print (people[:3])
print (people[7:])

print (people[::2])
print (people[1::2])

print (people[::-1])    # reversed list

# lists are mutable - i.e. I can add new items to it
people[0] = "ALICE"
people.append("Karen")

index = people.index("Fred")
print (index)

people.remove("Fred")

print (people)













