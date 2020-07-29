# Name Error
print(z)

# Key Error
x = {'one': 0}
print(x['two'])

# Index Error
x = [1, 2, 3]
print(x[3])

# Value Error
print(int('one'))

# Zero Division Error
print(3 / 0)

# Error Handling
try:
    print(3 / 0)
except NameError:
    print('Name Error Detected')
except ValueError:
    print('Value Error Detected')
except Exception:
    print('Other Error')

# Read File
f = open('sample.txt')
print(f.read())
f.close()
print('-------------------------------------')

# Also Read File
with open('sample.txt') as f:
    for line in f:
        print(line, end='')
print('\n-------------------------------------')

# Write File
with open('sample.txt', 'w') as f:
    f.write('Line 1\n')
    f.write('Line 2\n')

# Append File
with open('sample.txt', 'a') as f:
    f.write('Line 3\n')
    f.write('Line 4\n')