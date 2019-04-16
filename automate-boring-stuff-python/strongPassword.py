#! python3
# strongPassword.py - Find is your password is strong.

import re

password = input('Introduce your password: ')

find_upper = re.compile(r'[A-Z]').findall(password)
find_lower = re.compile(r'[a-z]').findall(password)
find_d = re.compile(r'\d').search(password)

if find_upper and find_lower and find_d and len(password) >= 8:
    print('Your password is strong.')
else:
    print('Your password is NOT strong.')
