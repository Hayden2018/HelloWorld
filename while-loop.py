# Create and index a list
a = [1, 2, 3]
print(a)
print(a[0])
print(a[1])
print(a[2])
print('-------------------------------------')

# List with different variable types
b = ['Hello', 'World', 2020]
print(b[0])
print(b[1])
print(b[2])
print('-------------------------------------')

# List within list
c = [[3, 4], 5]
print(c[0])
print(c[1])
print(c[0][0])
print('-------------------------------------')

# Print the length of list
print(len(b))
print(len(c))
print('-------------------------------------')

# List addition
d = a + b
print(d)
print('-------------------------------------')

# Append to a list
a.append(5)
print(a)
a.append('Hi')
print(a)
print('-------------------------------------')

# While loop with list
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
print('-------------------------------------')

# Calculate 1, 1+2, 1+2+3, 1+2+3+...+10
result = []
j = 1
sum = 0
while j <= 10:
    sum = sum + j
    result.append(sum)
    j = j + 1
print(result)

