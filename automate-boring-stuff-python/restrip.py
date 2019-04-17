#! python3
# restrip.py - regex version of strip() method.

# TOFIX:
# Fails with 'o' and ' hello' with string 'hello world hello'

import re
import sys

words_regex = re.compile(r'(\w+)')

def strip(string, char=None):
    if char != None:
        words_regex = re.compile(r'%s' % char)

    return words_regex.sub('',string)

# Delete only a matched string in string
if len(sys.argv) == 3:
    print(repr(strip(sys.argv[1], sys.argv[2])))

# Delete whitespace characters from beginning and end