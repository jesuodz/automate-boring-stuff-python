#! python3
# delUnneded.py - Find and delete exceptionally large files

import os
from os.path import join, getsize

max_size = 100000000

folders = []
for root, dirs, files in os.walk( os.getcwd() ):

    path, size = (root, sum([getsize( join(root,file) ) for file in files]))

    if size > max_size:
        folders.append( path )

print("Folders to delete: %s" % len(folders))

input()
