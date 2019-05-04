#! python3

import re
madlibs = open('madlib1.txt').read()

regex = re.compile(r'\w+|\W?')

words = regex.findall(madlibs)

def new_word(w):
    word = input('Enter a new word ( %s ): ' % (w.lower()))
    return word

for WORD in words:
    if WORD == 'ADJECTIVE':
        words[words.index(WORD)] = new_word(WORD)
    if WORD == 'VERB':
        words[words.index(WORD)] = new_word(WORD)
    if WORD == 'NOUN':
        words[words.index(WORD)] = new_word(WORD)

text = ''.join(words)

print("\nNew text:")
print(text)

new_madlib = open('madlib1-new.txt', 'w')
new_madlib.write(text)

new_madlib.close()
