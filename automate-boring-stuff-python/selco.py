#! python3
# selcopy.py - Copy files with a certain extension

import shutil
import re
import os
from os.path import join

# Create a regex that matches these file extensions.
extens = input('Extensions (separated by commas): ').split(',')
pattern_format = "|".join( ["\.%s" for extension in extens] )
extens_pattern = pattern_format % tuple(extens)

regexPattern = re.compile(r'(^.*?)(%s)$' % extens_pattern)

if not os.path.isdir('selections'):
    os.mkdir('selections')
else:
    print('\n"selections" directory already exits.')
    print('Copying files into existing folder.\n')

fls_copies = 0
for root, dirs, filenames in os.walk( os.getcwd() ):   

    for filename in filenames:
        file = regexPattern.search(filename)

        if file == None:
            continue

        src = join(root, file.group())

        print('Copying "%s" into "selections"' % file.group() )
        shutil.copy(src, 'selections')
        fls_copies += 1

    # Don't visit "selections" subfolder
    if 'selections' in dirs:
        dirs.remove('selections') 

print("\n%s files copied." % fls_copies )
input('Press "ENTER" to quit.')
