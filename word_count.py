# word_count.py

# count the number of words / lines / characters in a file

import sys

print ("Word counter")
print (sys.argv)
try:
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        lines = f.readlines()
        characters = 0
        word_count = 0

        for line in lines:
            characters = characters + len(line)

            words = line.split()
            word_count = word_count + len(words)

        print (f"lines = {len(lines)}")
        print (f"characters = {characters}")
        print (f"words = {word_count}")


except:
    print ("Usage:")
    print ("python word_count.py FILE")



