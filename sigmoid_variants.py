# sigmoid_variants.py
# Show different ways to express the derivative of sigmoid function.
import math

zp = 5

def op(x):
    return 1 / (1 + math.exp(-x))

def op_der(x):
    return math.exp(-x) / ( math.pow(1 + math.exp(-x), 2) )

def dop(x):
    return op(x) * (1 - op(x))

def dope(x):
    return x * (1.0 - x)

print('Activation function %s' % op(zp))
print('Derivative Op: %s' % op_der(zp))
print('Another derivative Op: %s' % dop(zp))

dope_res = dope( op(zp) )
print('Another one: %s' % dope_res)
print(op_der(zp) > dop(zp))

are_same = dop(zp) == dope_res
print('Is dop == dope?: %s' % are_same)
