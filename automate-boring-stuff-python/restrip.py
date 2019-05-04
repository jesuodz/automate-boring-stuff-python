#! python3
# restrip.py - regex version of strip() method.

# TOFIX:
# Fails with 'o' and ' hello' with string 'hello world hello'

import re
import sys

word_re = re.compile(r'\S+((\s+\S+)?)+')

def strip(s, c):
    # Delete whitespace characters from beginning and end
    if not c: return word_re.search(s).group()

if len(sys.argv) >= 1:
    string = sys.argv[1]
    char = None if len(sys.argv) == 2 else sys.argv[2]

    print(repr(strip(sys.argv[1], char)))
