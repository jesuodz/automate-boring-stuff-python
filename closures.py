#! python3

"""
def power(N):
    def f2(X):
        return X ** N
    return f2
"""

def power(N):
    return lambda X: X ** N

f = power(2)

samples = [str(f(n)) for n in range(5)]
print("Power by 2: |", ' | '.join(samples))
