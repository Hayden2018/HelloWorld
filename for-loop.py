# for-loop with list
x = [1, 3, 5, 7, 9]
for i in x:
    print(i)
print('-------------------------------------')

# for-loop with range iterator
for i in range(6):
    print(i, end='')
print('\n------------------')
for j in range(6, 12):
    print(j, end='')
print('\n------------------')
for k in range(6, 12, 2):
    print(k, end='')
print('\n-------------------------------------')

# for-loop with enumerate
for i, j in enumerate(x):
    print(i, j)
print('-------------------------------------')

# looping two list togather
a = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(x, a):
    print(i, j)
print('-------------------------------------')

# list comprehension
z = [2, 4, 6, 8, 10]
c = [i + j for i, j in zip(z, x)]
print(c)






