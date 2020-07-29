# Superclass
class Animal:

    def __init__(self):
        self.voice = '...' 
        self.age = 1

    def shout(self):
        print(self.voice)

    def __str__(self):
        raise NotImplementedError

# Subclass
class Cat(Animal):

    def __init__(self):
        super().__init__()
        self.voice = 'MEOW~'

    def __str__(self):
        return 'A ' + str(self.age) + ' years old cat'

    def catch_mouse(self):
        print('A mouse was caught!')

# Create the objects from class
a = Animal()
c = Cat()

# Difference behaviour in subclass and superclass
a.shout()
c.shout()

a.catch_mouse()
c.catch_mouse()

# Check subclass / instance relation
print(isinstance(c, Animal))
print(issubclass(Animal, Cat))