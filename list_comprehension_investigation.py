# list_comprehension_investigation.py


names = ["alice", "bob", "carol", "dan"]

# this is not how we would do this in python
capitalised_names = []

for name in names:
    capitalised_names.append(name.capitalize())

print (names)
print (capitalised_names)


# pythonic way - use list comprehension

capitalised_names = [name.capitalize() for name in names]

print (names)
print (capitalised_names)


# you can filter a list using a list comprehension

numbers = [1, 2, 5, 3, 4, 5, 6, 7, 10, 7]

big_numbers = [number for number in numbers if number >= 5]

print (numbers)
print (big_numbers)

even_numbers = [number for number in numbers if number % 2 == 0]

print (even_numbers)

# you can have two (or more) for loops 

colours = ["red", "green", "blue"]
products = ["pen", "pencil", "paint"]

product_options = [f"{colour} {product}" for colour in colours for product in products]

print (product_options)













