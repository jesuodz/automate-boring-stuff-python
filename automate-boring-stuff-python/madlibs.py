#! python3

import re
madlibs = open('madlib1.txt').read()

regex = re.compile(r'\w+|\W?')

words = regex.findall(madlibs)

for WORD in words:

    if WORD == 'ADJECTIVE':
        ask = input('Enter an adjective:\n')
        words[words.index(WORD)] = ask
    if WORD == 'VERB':
        ask = input('Enter an verb:\n')
        words[words.index(WORD)] = ask
    if WORD == 'NOUN':
        ask = input('Enter an noun:\n')
        words[words.index(WORD)] = ask

text = ''.join(words)

print()
print("New text:")
print(text)

new_madlib = open('madlib1-new.txt', 'w')
new_madlib.write(text)

new_madlib.close()
