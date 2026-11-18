import pygame as py 
from src.config import *
from src.game import *
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
    class PAWN:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-pawn.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    class BISHOP:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-bishop.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    class KNIGHT:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-knight.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    class QUEEN:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-queen.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    class KING:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-king.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))
        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    class ROOK:
        def __init__(self, case, color):
            self.case = case
            self.color = color
            #image
            self.piece = py.image.load(f"images/{self.color}-rook.png").convert_alpha()
            self.piece = py.transform.smoothscale(self.piece, (SIZE, SIZE))

        def blitPiece(self, screen, board):
            coord = board.argWhere(self.case)
            screen.blit(self.piece, coord)
    
    def add_pieces(self):
        for n in self.position:
            name = n[6:]
            if name == "pawn":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.PAWN(pos, self.color)
                    self.pieces.append(piece)
            elif name == "bishop":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.BISHOP(pos, self.color)
                    self.pieces.append(piece)

            elif name == "knight":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.KNIGHT(pos, self.color)
                    self.pieces.append(piece)
            elif name == "rook":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.ROOK(pos, self.color)
                    self.pieces.append(piece)
            elif name == "king":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.KING(pos, self.color)
                    self.pieces.append(piece)
            elif name == "queen":
                liste_pos = self.position[n].split()
                for pos in liste_pos:
                    piece = self.QUEEN(pos, self.color)
                    self.pieces.append(piece)
            

    
   

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

    board = BOARD()
    board.start()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        

        screen.fill(BACK)
        drawBoard(screen)
        for i in white.pieces:
            i.blitPiece(screen, board)
        py.display.flip()

    py.quit()

if __name__=="__main__":
    main()