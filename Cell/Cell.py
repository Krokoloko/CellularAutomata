import random as rand

class Cell:
    def __init__(self,state,neighbours):
        self.state = state
        
        #reletive positions from the cell
        self.neighbours = neighbours
