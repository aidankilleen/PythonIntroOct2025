# string_investigation.py

# printing
# input


name = "Aidan"
print (name.lower())
name = input("what is your name?")

print (name)


# multi-line strings

message = """
this
is
a
multiline
string
"""

print (message)

# single quotes and double quotes are interchangable
name = "Aidan"
name = 'Aidan'

message = 'press the "red" button'

print (message)

name = "John O'Sullivan"
print (name)

# escape characters

print ("line1\nline2\nline3\n") # \n = newline character

print ("column 1\tcolumn2\tcolumn3") # \t = tab character

print ("press the \"red\" button")

path = "C:\\users\\aidan\\myfiles\\file.txt"

print (path)

# formatted strings - f-strings
answer = 1234

print ("the answer is " + str(answer))
print (f"the answer is {answer}")


a = 10
b = 20

print ("" + str(a) + " + " + str(b) + " = " + str(a+b))
print (f"{a} + {b} = {a+b}")    # Note - you can put in an expression

answer = 10
# it is pythonic to use inline conditionals in f strings
print (f"the answer is {"big" if answer > 5 else "small"}")


















































