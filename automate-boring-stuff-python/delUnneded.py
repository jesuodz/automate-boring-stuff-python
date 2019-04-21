#! python3
# delUnneded.py - Find and delete exceptionally large files

import os
from os.path import join, getsize

max_size = 100000000

folders = []
file_paths = []

for root, dirs, files in os.walk( os.getcwd() ):

    path, size = (root, sum([getsize( join(root,file) ) for file in files]))

    if size > max_size:
        folders.append( path )

    for filename in files:
        file_path = join(root, filename)

        if getsize(file_path) > max_size:
            file_paths.append(file_path)

print("Folders to delete: %s" % len(folders))
print("Files to delete: %s" % len(file_paths))

input()
