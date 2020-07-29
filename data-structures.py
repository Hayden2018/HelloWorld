# Dictionary
person = {'name': 'Chris', 'age': 20}
print(type(person))
print(person)
print(person['name'])
print(person['age'])
print('-------------------------------------')

# Dictionary operation
person['gender'] = 'Male'
person['favourite color'] = ['Green', 'Yellow']
person[37] = 'favourite number'
del person['age']
print(person['favourite color'])
print(person['gender'])
print('age' in person)
print('-------------------------------------')

# Tuple
t = (1, 2, 3)
print(type(t))
print(t)
print(t[0])
print('-------------------------------------')

# Tuple as function return
def f():
    return 4, 5, 6
x = f()
print(type(x))
a, b, c = x
print(a, b, c)
print('-------------------------------------')

# Set
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 = s1.union(s2)
print(type(s1))
print(s1)
print('-------------------------------------')

# Set operation
s2.add(5)
s2.add(2)
print(s2)
print(3 in s2)
print(9 in s2)



