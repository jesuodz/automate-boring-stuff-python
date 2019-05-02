#! python3

""" Original
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1

if found:
    print('at index', i)
else:
    print(X, 'not found')
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

"""
Solution to (A):
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break;
    else:
        i = i+1
else:
    print(X, 'not found')
"""

"""
Solution to (B):
for n in L:
    if 2 ** X == n:
        print('at index', L.index(n))
        break;
else:
    print(X, 'not found')
"""

"""
Solution to (C)
if 2 ** X in L:
    print('at index', X)
else:
    print(X, 'not found')
"""

"""
Solution to (D)
l = list()
for n in range(X):
    l.append(2 ** n)

lx = [ 2 ** n for n in range(X)]

print(lx == l)
"""
