#! python3
# research.py - Look for regex patterns in .txt files

import re, os

files = [file for file in os.listdir() if file.endswith('txt')]

pattern = input('Regex pattern: ')
regex = re.compile(r'%s' % pattern)

# TODO: Loop through all files in a efficient mannerk

# TODO: Find and save matches

""" IDEA: Save matches by file and line in a dict
         { 'FILE' : ['LINE1', 'LINE2', 'LINE4'], ...}
"""
