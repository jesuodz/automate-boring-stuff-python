#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import os
import shutil
import re

date_pattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)
    
    if mo == None:
        continue
    
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_filename = (before_part + day_part + '-' + month_part + '-' +
                     year_part + after_part)

    abs_working_dir = os.path.abspath('.')
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    print('Renaming "%s" to "%s"' % (amer_filename, euro_filename))
    shutil.move(amer_filename, euro_filename)
else:
    print('0 files to rename.')
