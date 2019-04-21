#! python3
# delUnneded.py - Find and delete exceptionally large files

import os
from os.path import join, getsize

folders = []
for root, dirs, files in os.walk( os.getcwd() ):
    
    folders.append( (root, sum([getsize( join(root,file) ) for file in files])) )

print(folders)
input()