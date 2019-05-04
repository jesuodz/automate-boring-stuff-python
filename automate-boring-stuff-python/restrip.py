#! python3
# restrip.py - regex version of strip() method.
# Usage:       python restrip.py "   textt ..  " - Strip trailing whitespaces.
#              python restrip.py "hello world" "hello "  - Strip later text.

import re
import sys

word_re = re.compile(r'\S+((\s+\S+)?)+')

def strip(s, c):
    # Delete whitespace characters from beginning and end
    if not c: return word_re.search(s).group()

    # Delete character from beginning and end
    char_re = re.compile(r'(^%s)|(%s$)' % (c, c))
    return char_re.sub('', s)

if len(sys.argv) >= 1:
    string = sys.argv[1]
    char = None if len(sys.argv) == 2 else sys.argv[2]

    print(repr(strip(sys.argv[1], char)))
