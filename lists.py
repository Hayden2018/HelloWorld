# Negative indexing
x = [1, 2, 3, 4, 5, 6, 7]
m = x[-1]
n = x[-3]
print(m)
print(n)
print('--------------------------')

# List slicing
w = x[:3]
y = x[1:]
z = x[1:3]
print(w)
print(y)
print(z)
print('--------------------------')

# Built-in functions for list
x = [1, 4, 3, 5, 2, 7, 6]
print(sorted(x))
print(max(x))
print(min(x))
print('--------------------------')

# Insert to list
x.insert(3, 'Hi')
print(x)
print('------------------------')

# Remove from list
x.remove('Hi')
print(x)