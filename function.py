# Function with no return and argument
def f():
    print('I am calling a function!')
f()
print('-------------------------------------')

# Function with one argument and return
def square(x):
    return x**2
print(square(3))
print('-------------------------------------')

# Finction with multiple argument
def power(x, y):
    return x**y
print(power(2, 3))
print('-------------------------------------')

# Function with default argument
def say_hello(name="John"):
    print("Hello I am " + name)
say_hello("Marry")
print('-------------------------------------')

# Recursion
def factorial(z):
    if z == 1:
        return 1
    else:
        return z * factorial(z - 1)
print(factorial(5))
print('-------------------------------------')


