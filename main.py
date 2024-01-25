from models import * 
from settings import * 
from utils import *
import sys

def tegn_viduet(spille_brett, menneske):
    vindu = spille_brett.vindu
    spille_brett.vindu.fill("black")
    pg.draw.rect(vindu, FRISONE_FARGE, spille_brett.venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,spille_brett.høyre_frisone)
    #pg.draw.rect(spille_brett.vindu, STOLPE_FARGE, main_board.stolpe)
    menneske.plassering(MENNESKE_BREDDE, MENNESKE_HØYDE, vindu)
    pg.display.update()

def mennesket_kontroll(mennesket, fart): 
    keys = pg.key.get_pressed() 
    if keys[pg.K_w]:
        mennesket.beveg(fart, "opp")
    if keys[pg.K_s]:
        mennesket.beveg(fart, "ned")
    if keys[pg.K_d]:
        mennesket.beveg(fart, "høyre")
    if keys[pg.K_a]:
        mennesket.beveg(fart, "venstre")

def main():
    fart = 5
    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100, fart)
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        mennesket_kontroll(menneske, fart)
        tegn_viduet(spille_brett, menneske)



if __name__ == "__main__":
    main()