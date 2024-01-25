from models import * 
from settings import * 
from utils import *
import sys



def tegn_viduet(spille_brett, menneske, spøkelse):
    vindu = spille_brett.vindu
    spille_brett.vindu.fill("black")
    pg.draw.rect(vindu, FRISONE_FARGE, spille_brett.venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,spille_brett.høyre_frisone)
    #pg.draw.rect(spille_brett.vindu, STOLPE_FARGE, main_board.stolpe)
    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)
    for obj in spille_brett.objekter:
        obj.plassering(obj.BREDDE, obj.HØYDE, vindu)
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

def spøkelse_kontroll(spøkelse, ret, frisone_v, frisone_h):
    spøkelse.endre_retning(frisone_v, frisone_h)
    if ret == "venstre":
        spøkelse.flytt(-spøkelse.vx, -spøkelse.vy)
    elif ret == "høyre":
        spøkelse.flytt(spøkelse.vx, spøkelse.vy)
    elif ret == "ned":
        spøkelse.flytt(-spøkelse.vx, spøkelse.vy)
    elif ret == "opp":
        spøkelse.flytt(spøkelse.vx, -spøkelse.vy)
        
        
    
def main():
    mennesket_fart = 5
    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100, mennesket_kontroll)
    spøkelse = Spøkelse(500,400)
    run = True
    start_spøkelse_retning = tilfeldig_retning()
    print(start_spøkelse_retning)
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        mennesket_kontroll(menneske, mennesket_fart)
        spøkelse_kontroll(spøkelse, start_spøkelse_retning, spille_brett.venstre_frisone, spille_brett.høyre_frisone)
        tegn_viduet(spille_brett, menneske, spøkelse)



if __name__ == "__main__":
    main()