# Return a list of divisors of an integer n
def find_divsor(n):
    i = n // 2
    divisors = []
    while i > 1:
        if n % i == 0:
            divisors.append(i)
        i = i - 1
    return divisors

# Get user input and pass to function
s = input('Please input a integer:')
x = int(s)
divisors = find_divsor(x)

# Print out the result
if len(divisors) == 0:
    print(x, 'has no divisors other than one and itself.')
else:
    print(x, 'has the following divisors:')
    for d in divisors:
        print(d)