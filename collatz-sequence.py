# Collatz secuence
import sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    
    print(result)
    return result

try:
    n = int(input('Enter number: '))
except ValueError:
    sys.exit('Error: enter an integer.')

while n != 1:
    n = collatz(n)
