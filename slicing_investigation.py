# slicing_investigation.py


message = "this is a string for testing"

print (message)
print (len(message))

print (message[0]) # first character
print (message[1]) # second character

print (message[-1]) # last character

for c in message:
    print (c)

# split
words = message.split()

print (words)

for word in words:
    print (word)

words.reverse()

for word in words:
    print (word)

# slicing

print ("*" * 30)

print (message)
print (message[5:16])

print (message[:16]) # start to 16
print (message[16:]) # 16 to the end

# inclusive of the first index
# exclusive of the second index
print (message[0:4])


numbers = "12345678910"

# start (inclusive)
# stop (exclusive)
# step 
print (numbers[0:10:2])

# negative index
print (numbers[-1])

# from start to end in steps of 2
print (numbers[::2])

# very pythonic way of reversing a string
# a negative step value means go in reverse
print (numbers[::-1])









































