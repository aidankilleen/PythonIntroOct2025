# folder_size.py

import os
import sys

if len(sys.argv) < 2:
    print ("Usage:")
    print ("python folder_size.py DIR")
    exit (1)

directory = sys.argv[1]
if os.path.exists(directory) == False:
    print ("Folder doesn't exist")
    exit(2)

size = 0

for (path, _, filenames) in os.walk(directory):

    for f in filenames:
        file_path = os.path.join(path, f)
        if (os.path.isfile(file_path)):
            size = size + os.path.getsize(file_path)

print (f"Total size of {directory} = {size}")

