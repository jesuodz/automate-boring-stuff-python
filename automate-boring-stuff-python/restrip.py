#! python3
# restrip.py - regex version of strip() method.

# TOFIX:
# Fails with 'o' and ' hello' with string 'hello world hello'

import re
import sys

spce_regex = re.compile(r'\s+')

def strip(s, char):
    # Delete whitespace characters from beginning and end
    return spce_regex.sub('', string)

if len(sys.argv) >= 1:
    string = sys.argv[1]
    char = None if len(sys.argv) == 2 else sys.argv[2]

    print(repr(strip(sys.argv[1], char)))
