#! python3
# delUnneded.py - Find and delete exceptionally large files

import os
from os.path import join, getsize

max_size = 100000000 # 100mb

folders = []
lst_files = []

for root, dirs, filenames in os.walk( os.getcwd() ):

    dir_path, size = (root, sum(
        [getsize( join(root,filename) ) for filename in filenames
    ]))

    if size > max_size:
        folders.append( dir_path )

    for filename in filenames:
        file_path = join(root, filename)

        if getsize(file_path) > max_size:
            lst_files.append(file_path)

if len(folders) != 0:
    print('%s folders to delete.' % len(folders))
    for folder in folders:
        print(folder)
else:
    print('0 folders to delete.')

print()

if len(lst_files) != 0:
    print('%s files to delete.' % len(lst_files))
    for file in lst_files:
        print(file)
else:
    print('0 files to delete.')

input('Press ENTER to quit.')
