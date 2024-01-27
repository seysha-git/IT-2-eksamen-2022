from settings import * 
from utils import *
import sys
import random as rd

def lag_hindringer(antall_start_hinderinger, spille_brett):
    while antall_start_hinderinger < 3:
        ikke_kollidert_hinder = False
        while not ikke_kollidert_hinder:
            ny_hinder = Hindering()
            ikke_kollidert_hinder = True
            if ny_hinder.rekt.colliderect(spille_brett.venstre_frisone) or ny_hinder.rekt.colliderect(spille_brett.høyre_frisone):
                ikke_kollidert_hinder = False
            hinderinger = list(filter(lambda obj: obj.navn == "hindering", spille_brett.objekter))
            ikke_kollidert_hinder = sjekk_innen_kollisjon(hinderinger, ny_hinder, ikke_kollidert_hinder)
            spille_brett.legg_till_objekt(ny_hinder)
            antall_start_hinderinger += 1


def main():

    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    spøkelse = Spøkelse(tilfeldig_retning())
    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)

    antall_start_hinderinger = 0
    antall_start_sauer = 0

    run = True
    while run:
        clock.tick(FPS)
        
        while antall_start_hinderinger < 3:
            ikke_kollidert_hinder = False
            while not ikke_kollidert_hinder:
                ny_hinder = Hindering()
                ikke_kollidert_hinder = True
                if ny_hinder.rekt.colliderect(spille_brett.venstre_frisone) or ny_hinder.rekt.colliderect(spille_brett.høyre_frisone):
                    ikke_kollidert_hinder = False
                hinderinger = list(filter(lambda obj: obj.navn == "hindering", spille_brett.objekter))
                ikke_kollidert_hinder = sjekk_innen_kollisjon(hinderinger, ny_hinder, ikke_kollidert_hinder)
                spille_brett.legg_till_objekt(ny_hinder)
                antall_start_hinderinger += 1 

        while antall_start_sauer < 3:
            ikke_kollidert_sau = False
            while not ikke_kollidert_sau:
                ny_sau = Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50))
                sauer = list(filter(lambda obj: obj.navn == "sau", spille_brett.objekter))
                ikke_kollidert_sau = True
                ikke_kollidert_sau = sjekk_innen_kollisjon(sauer, ny_sau, ikke_kollidert_sau)
                spille_brett.legg_till_objekt(ny_sau)
                antall_start_sauer += 1
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        
        tegn_viduet(spille_brett)
        #
if __name__ == "__main__":
    main()



