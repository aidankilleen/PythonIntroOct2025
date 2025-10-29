# file_size.py
# command line utility which will tell me how big a file is

import sys
import os

print ("folder_size.py")
# print (sys.argv)

if len(sys.argv) < 2:
    print ("Usage:")
    print ("python file_size.py FILE")
    exit(1)

filename = sys.argv[1]

if os.path.exists(filename) == False:
    print (f"{filename} not found")
    exit(2)

size = os.path.getsize(filename)
print (f"{filename} is {size} bytes")

       





