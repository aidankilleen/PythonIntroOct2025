# error_investigation.py

# exception handling

# try:
#     do_something()
#     do_something_else()

# except FileExistsError:
#     #

# except NotADirectoryError:

# except Exception:







# glass is half empty
# constantly checking for errors
# hard to see the actual code
# r = do_something()

# if r==1:
#     # network error
# elif r ==2:
#     # user error
# elif r == 3:
#     # file error
# else:
#     # everything ok

# r = do_something_else()
# if r==1:
#     # network error
# elfif r ==2:
#     # user error
# elif r == 3:
#     # file error
# else:
#     # everything ok








from random import randint


print ("Error Investigation")

a = 10
b = 0
numbers = [1, 2, 3, 4, 5]
text = "ten"

r = randint(1, 4)

try:
    if r==1:
        answer = a / b
    elif r==2:
        answer = int(text)
    elif r ==3:
        answer = numbers[5]
    else:
        answer = 42 
except ZeroDivisionError:
    print ("You can't divide by zero")
    answer = a
except IndexError:
    print ("You can't access an item outside the list")
    answer = numbers[-1]
except Exception as e:
    # catch all exception hanlder - any runtime error that doesn't have a except block 
    # will trigger this code
    print ("something went wrong")
    print (str(e))
    answer = 0

print (f"The answer is {answer}")

print("finished")