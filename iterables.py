# Iterating string
for c in 'Hi-World':
    print(c)
print('----------------')

# User-defined iterator
def squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1

for j in squares(5):
    print(j)
print('----------------')

# Make a class into an iterable
class Cube:

    def __init__(self):
        pass

    def __iter__(self):
        i = 1
        while i <= 5:
            yield i ** 3
            i += 1

cube = Cube()
for j in cube:
    print(j)
print('----------------')

# Using itertools from the standard library
from itertools import combinations, product

x = [1, 2, 3]
y = ['a', 'b', 'c']
for t in combinations(x, 2):
    print(t)
print('----------------')
for t in product(x, y):
    print(t)
print('----------------')