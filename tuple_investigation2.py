# tuple_investigtion2.py


names_list = ["Alice", "Bob", "Carol", "Dan"]

names_tuple = ("Alice", "Bob", "Carol", "Dan")


# lists are mutable
names_list[0] = "ALICE"

# tuples are immutable
# names_tuple[0] = "ALICE"

# A tuple is an immutable list



def process_list(numbers):

    max_number = max(numbers)
    min_number = min(numbers)

    # return multiple values from a function
    # using a tuple
    return (max_number, min_number)


numbers = [1, 4, 3, 2, 5, 7, 99,8, 4]
answer = process_list(numbers)

print (answer)







