#! python3
# selcopy.py - Copy files with a certain extension

# TODO: Copy the matched file in the right directory.
import shutil
import re
import os

# Create a regex that matches these file extensions.
extens = input('Extensions (separated by commas): ').split(',')
pattern_format = "|".join( ["\.%s" for extension in extens] )
extens_pattern = pattern_format % tuple(extens)

regexPattern = re.compile(r'(^.*?)(%s)$' % extens_pattern)

if not os.path.isdir('selections'):
    os.mkdir('selections')
else:
    print('\n"selections" directory already exits. Copying files into existing folder.\n')

for folder, subfolder, filename in os.walk( os.getcwd() ):
    print(filename)
    # file = regexPattern.search(filename)

    # if file == None:
    #     continue
    
    # print('Copying "%s" into "selections"' % file.group() )
    # shutil.copy(file.group(), 'selections')

# TODO: Copy each directory inside the current working directory

# TODO: Copy the matched file in the right directory.
