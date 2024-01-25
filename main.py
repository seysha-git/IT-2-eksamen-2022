from models import * 
from settings import * 
from utils import *
import sys

def draw_window(main_board):
    main_board.vindu.fill("black")
    pg.draw.rect(main_board.vindu, FRISONE_FARGE, main_board.venstre_frisone)
    pg.draw.rect(main_board.vindu, FRISONE_FARGE,main_board.høyre_frisone)
    #pg.draw.rect(main_board.vindu, STOLPE_FARGE, main_board.stolpe)
    pg.display.update()



def main():
    main_board = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        draw_window(main_board)



if __name__ == "__main__":
    main()