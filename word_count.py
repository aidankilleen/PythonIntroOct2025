# word_count.py
# count the number of words / lines / characters in a file

# how do we implement 
# options
# -l - return the line count
# -c - return the character count
# -w - return the word count

import sys

print ("Word counter")
try:
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        line_count = f.readlines()
        character_count = 0
        word_count = 0

        for line in line_count:
            character_count += len(line)
            words = line.split()
            word_count += len(words)

        print (f"lines = {len(line_count)}")
        print (f"characters = {character_count}")
        print (f"words = {word_count}")

except FileNotFoundError:
    print (f"File {file_name} not found")
except:
    print ("Usage:")
    print ("python word_count.py FILE")



