# Defining classes
class Person:

    def __init__(self, name):
        self.name = name
        self.hp = 10

    def shout(self):
        print(self.name, ': Ahhhhhh')

class Monster:

    def __init__(self):
        self.hp = 10
        self.power = 2

    def laugh(self):
        print('Monster : HA! HA!')

    def hit(self, person):
        person.hp -= self.power
        person.shout()
        self.laugh()

# Creating objects from classes
m = Monster()
p = Person('Mary')

# Objects interact with each other
print('Person\'s health = ', p.hp)
m.hit(p)
print('Person\'s health = ', p.hp)
