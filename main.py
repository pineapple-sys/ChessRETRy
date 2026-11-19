import pygame as py 
from src.config import *
from src.game import *
class Piece:
        def __init__(self, case: str,name: str):
            self.case = case
            self.name = name
            #image
            self.piece = py.image.load(f"images/{self.name}.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
class PLAYER:
    def __init__(self, color: str):
        self.color = color
        self.position = {}
        self.pieces = []
    def start(self):
        if self.color == 'white':
            self.position = white_start
        else:
            self.position = black_start
    

    def add_pieces(self):
        for n in self.position:
            
            liste_pos = self.position[n].split()
            for pos in liste_pos:
                piece = Piece(pos,n)
                self.pieces.append(piece)
            
                

    def blitPiece(self, screen, board):
            for piece in self.pieces:
                coord = board.argWhere(piece.case)
                screen.blit(piece.piece, coord)
            
def drawBoard(screen):
    count = 0
    for i in range(0, WIDTH, SIZE):
        for j in range(0, HEIGHT, SIZE):
            if count %2 ==0:
                py.draw.rect(screen, LIGHT, (i,j,SIZE, SIZE))
            else:
                py.draw.rect(screen, DARK, (i,j,SIZE, SIZE))
            count +=1
        count += 1
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))

    running = True
    white = PLAYER("white")
    white.start()
    white.add_pieces()
    black = PLAYER("black")
    black.start()
    black.add_pieces()

    board = BOARD()
    board.start()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        

        screen.fill(BACK)
        drawBoard(screen)
        
        white.blitPiece(screen, board)
        black.blitPiece(screen, board)
        py.display.flip()

    py.quit()

if __name__=="__main__":
    main()