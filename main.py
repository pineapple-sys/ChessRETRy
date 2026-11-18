import pygame as py 
from src.config import *
from src.game import *

def blitPiece(screen, board):
    for name in position:
        liste_pos = position[name].split()
        for pos in liste_pos:
            coord = board.argWhere(pos)
            piece = py.image.load(f"images/{name}.png").convert_alpha()
            piece = py.transform.smoothscale(piece, (SIZE, SIZE))
            screen.blit(piece, coord)

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
    
    board = BOARD()
    board.start()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        

        screen.fill(BACK)
        drawBoard(screen)
        blitPiece(screen, board)
        py.display.flip()

    py.quit()

if __name__=="__main__":
    main()