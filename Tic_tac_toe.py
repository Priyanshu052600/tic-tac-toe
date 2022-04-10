import numpy as np

class Game:
    def __init__(self):
        self.cells = np.array(["" for x in range(9)])
        self.turn = 0
        self.symbols = ['O', 'X']
        self.running = False
    
    def display(self):
        print("{} | {} | {}".format(self.cells[0], self.cells[1], self.cells[2]))
        print("------")
        print("{} | {} | {}".format(self.cells[3], self.cells[4], self.cells[5]))
        print("-------")
        print("{} | {} | {}".format(self.cells[6], self.cells[7], self.cells[8]))
        
    def get_player_turn(self):
        if self.turn % 2 == 0:
            return self.symbols[0]
        else:
            return self.symbols[1]
        
    def check_playable_field(self, cell_number):
        allowed = np.where(self.cells == "")
        allowed = np.array(allowed)
        if cell_number in allowed:
            return True
        else:
            return False
        
    def update_cell_and_turn(self, cell_number, symbol):
        self.cells[cell_number] = symbol
        self.turn += 1
        
    def is_winner(self, symbol):
        win_combinations=((0,1,2),(3,4,5),(6,7,8),(6,3,0),(7,4,1),(8,5,2),(6,4,2),(8,4,0))
        for wc in win_combinations:
            if self.cells[wc[0]] == symbol and self.cells[wc[1]] == symbol and self.cells[wc[2]] == symbol:
                return True
            else:
                return False  
           
    def reset(self):
        self.cells = np.array(["" for x in range(9)])
        self.turn = 0
            