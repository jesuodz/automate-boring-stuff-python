#! python3

spam = {
    3: 'c',
    2: 'b',
    1: 'a',
    -1: 'k'
}

for item in sorted(spam.items(), reverse=True):
    print(item, end=' ')
