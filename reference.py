# Immutable objects
x = 1
b = True
s = 'Hello World'

x = 1
y = x
y = 2
print(x)
print('-------------------')

# Mutable objects
a = [1, 2, 3]
d = {'name': 'Peter'}
s = {4, 5, 6}
# User classes are usually mutable

x = [1, 2, 3]
y = x
y[0] = 4
print(x)
print('-------------------')

x = [1, 2, 3]
y = x
y = [4, 5, 6]
print(x)
print('-------------------')

# Using copy and deepcopy
from copy import copy, deepcopy

x = [1, 2, 3]
y = copy(x)
y[0] = 4
print(x)
print('-------------------')

x = [[1, 2], 3]
y = copy(x)
y[0][0] = 4
print(x)
print('-------------------')

x = [[1, 2], 3]
y = deepcopy(x)
y[0][0] = 4
print(x)
print('-------------------')

# Default arguments should not be mutable
def f(a=[]):
    print(len(a))
    a.append(1)

f()
f()