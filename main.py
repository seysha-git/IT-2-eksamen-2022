from settings import * 
from utils import *
import sys
import random as rd


def main():

    antall_start_hinderinger = 0
    antall_start_sauer = 0

    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    spøkelse = Spøkelse(tilfeldig_retning())

    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)

    while antall_start_hinderinger < 3:
        ny_hinder = Hindering()
        spille_brett.legg_till_objekt(ny_hinder)
        antall_start_hinderinger += 1
    while antall_start_sauer < 3:
        ny_sau = Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50))    
        spille_brett.legg_till_objekt(ny_sau)
        antall_start_sauer += 1

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        
        tegn_vinduet(spille_brett)
        #
if __name__ == "__main__":
    main()



