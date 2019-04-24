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

# TODO: Loop through all files in a efficient mannerk
for file in files:
    fhandler = open(file, 'r', encoding='utf-8')
    content = fhandler.read()

    print(regex.findall(content))
    fhandler.close()

# TODO: Find and save matches

""" IDEA: Save matches by file and line in a dict
         { 'FILE' : ['LINE1', 'LINE2', 'LINE4'], ...}
"""
