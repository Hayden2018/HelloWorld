# Import a module from standard library
import math
print(math.cos(0))
print('-----------------------')

# Import specific functions from standard library
from math import sin, cos
print(sin(0))
print(cos(0))
print('-----------------------')

# Import a specific function from standard library with renaming
from math import tan as tangent
print(math.tan(0.1234))
print(tangent(0.1234))
