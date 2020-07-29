class Board:

    def __init__(self):
        self.state = [[' ' for i in range(3)] for j in range(3)]
        # Dictionary for mapping user to list index
        self.x_coor = {a: i for i, a in enumerate('ABC')}
        self.y_coor = {n: i for i, n in enumerate('123')}

    # Return True if there is winner
    def have_winner(self):

        # Check rows and columns
        for i in range(3):
            non_empty = self.state[i][i] != ' '
            row = (self.state[i][0] == self.state[i][1]) and (self.state[i][1] == self.state[i][2])
            col = (self.state[0][i] == self.state[1][i]) and (self.state[1][i] == self.state[2][i])
            if non_empty and (row or col):
                return True

        # Check diagonals
        non_empty = self.state[1][1] != ' '
        d1 = (self.state[0][0] == self.state[1][1]) and (self.state[1][1] == self.state[2][2])
        d2 = (self.state[2][0] == self.state[1][1]) and (self.state[1][1] == self.state[0][2])
        if non_empty and (d1 or d2):
            return True
        else:
            return False
    
    # Place a move of the given player to the given position
    def move(self, player, pos):
        pos = pos.lstrip().upper()
        x = self.x_coor[pos[0]]
        y = self.y_coor[pos[1]]
        if self.state[y][x] == ' ':
            self.state[y][x] = player
        else:
            raise Exception
    
    # Return a string that display the state of the board
    def __str__(self):
        s = '  A   B   C\n'
        for i in range(3):
            s += str(i + 1) + ' '
            for j in range(3):
                s += self.state[i][j]
                if j != 2:
                    s += ' | '
            if i != 2:
                s += '\n  -- --- --\n'
        s += '\n'
        return s
        



    

    
