#! python3
# mkDatesFiles.py - Create `.txt` files with American MM-DD-YYYY date format
import random

n_files = input('How many files?: ')

def create_date():
    d = random.randint(1, 30)
    m = random.randint(1,12)
    y = random.randint(1900, 2099)

    return (m, d, y)

for n in range(int(n_files)):
    date = "-".join([str(i) for i in create_date()])

    file = open(date + '.txt', 'w')
    file.close()
