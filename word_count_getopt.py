# word_count.py
# count the number of words / lines / characters in a file

# how do we implement 
# options
# -l - return the line count
# -c - return the character count
# -w - return the word count

import getopt
import sys


def show_usage():
    print ("Usage:")
    print ("python word_count.py [OPTION...] FILE")
    print ("Options:")
    print ("-l - show number of lines")
    print ("-w - show number of words")
    print ("-c - show number of characters")

print ("Word counter")
try:
    argv = sys.argv[1:]
    (opts, files) = getopt.getopt(argv, "lcw")
    print (opts)

    opt_lookup = [opt for opt, _ in opts]

    print (opt_lookup)
    print ("=" * 50)
    print (files)
    
    #options = [option for option in sys.argv if option.startswith("-")]
    #files = [file_name for file_name in sys.argv[1:] if file_name.startswith("-") == False]

    file_name = files[0]

    with open(file_name, "r") as f:
        line_count = f.readlines()
        character_count = 0
        word_count = 0

        for line in line_count:
            character_count += len(line)
            words = line.split()
            word_count += len(words)

        if "-l" in opt_lookup:
            print (f"lines = {len(line_count)}")
        if "-c" in opt_lookup:
            print (f"characters = {character_count}")
        if "-w" in opt_lookup:
            print (f"words = {word_count}")

except IndexError:
    # D.R.Y.
    # Don't repeat yourself
    show_usage()

except FileNotFoundError:
    print (f"File {file_name} not found")
except Exception as ex:
    print (str(ex))

    show_usage()



