from random import randint

class Snake:

    colors = ['red', 'green', 'blue']
    art = '''
                    ____
                 .'`_ o `;__,
       .       .'.'` '---'  '            
       .`-...-'.'
        `-...-'
        '''

    def __init__(self, length):
        self.body = [Snake.colors[randint(0, 2)] for i in range(length)]

    # Overloading the len() function
    def __len__(self):
        return len(self.body)

    # Overloading the str() function
    def __str__(self):
        return Snake.art

    # Overloading the + operator
    def __add__(self, other):
        if type(other) != type(self):
            raise TypeError('Only snakes can be added togather')
        else:
            new_snake = Snake(0)
            new_snake.body = self.body + other.body
            return new_snake

    # Overloading the [] operator
    def __getitem__(self, index):
        return self.body[index]

s1 = Snake(3)
s2 = Snake(5)
print(len(s2))
print(s2)

s3 = s1 + s2
print(len(s3))
print(s3[0])