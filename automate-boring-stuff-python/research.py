#! python3
# research.py - Look for regex patterns in .txt files

import re
import os
from sys import exit

files = [file for file in os.listdir() if file.endswith('txt')]

if len(files) == 0: exit('No "*.txt" files found in folder.')

pattern = input('Regex pattern: ')
if len(pattern) == 0: exit('Pattern not long enough.')

regex = re.compile(r'%s' % pattern)

def search(file):
    """ Find occurrences in current file """
    occurr = list()

    for (offset, line) in enumerate(open(file, encoding='utf-8')):
        if regex.search(line): occurr.append(offset)
    return (occurr, file)

for item in map(search, files):
    if len(item[0]) == 0: continue
    print("Found %i occurrences from line(s) %s in file %s" %
         (len(item[0]), (item[0]), item[1]))
else:
    print("Found 0 occurrences in '.txt' files in current directory.")
