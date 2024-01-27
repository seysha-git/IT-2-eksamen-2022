from settings import * 
from utils import *
import sys
import random as rd

def main():
    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    antall_hinderinger = 3
    antall_sauer = 3
    antal_spøkelser = 1
    spøkelse = Spøkelse(tilfeldig_retning())
    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)
    run = True
    while run:
        clock.tick(FPS)
        while antall_hinderinger > 0:
            ikke_kollidert = False
            while not ikke_kollidert:
                hinder = Hindering()
                ikke_kollidert = True
                if hinder.rekt.colliderect(spille_brett.venstre_frisone) or hinder.rekt.colliderect(spille_brett.høyre_frisone):
                    print("kolliderte")
                    ikke_kollidert = False
            spille_brett.legg_till_objekt(hinder)
            antall_hinderinger -= 1
        while antall_sauer > 0:
            ikke_kollidert_sau = False
            while not ikke_kollidert_sau:
                ny_sau = Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50))
                ikke_kollidert_sau = True
                sauer = list(filter(lambda obj: obj.navn == "sau", spille_brett.objekter))
                for sau in sauer:
                    if ny_sau.rekt.colliderect(sau.rekt):
                        ikke_kollidert_sau = False
            spille_brett.legg_till_objekt(ny_sau)
            antall_sauer -= 1
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        tegn_viduet(spille_brett)




if __name__ == "__main__":
    main()



