import numpy as np
from src.config import *

class BOARD:
    def __init__(self):
        self.board = np.zeros((8,8), dtype="O")
    def start(self):
        for ordLetter in range(ord('a'), ord('h')+1):
            x = ordLetter-ord('a')
            for nb in range(1, 9):
                self.board[-nb, x] = f"{chr(ordLetter)}{nb}"
    def argWhere(self, case):
        coord = np.argwhere(self.board == case)[0]
        coord = (coord[1]*SIZE, coord[0]*SIZE)
        return coord





