from models import * 
from settings import * 
from utils import *
import sys
import random as rd



def tegn_viduet(spille_brett):
    vindu = spille_brett.vindu
    spille_brett.vindu.fill("black")
    pg.draw.rect(vindu, FRISONE_FARGE, spille_brett.venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,spille_brett.høyre_frisone)
    #pg.draw.rect(spille_brett.vindu, STOLPE_FARGE, main_board.stolpe)
    for obj in spille_brett.objekter:
        obj.plassering(vindu)
    pg.display.update()

def mennesket_kontroll(mennesket, hinderinger):
    up_hit, down_hit, left_hit, right_hit = False, False, False, False
    for hinder in hinderinger:
        if mennesket.rekt.colliderect(hinder.rekt):
            if hinder.x > mennesket.x:
                left_hit = True
                right_hit = False
            elif mennesket.x > hinder.x:
                right_hit = True
                left_hit = False
                print("triggerd")
            if hinder.y > mennesket.y:
                up_hit = True
                down_hit = False
            elif mennesket.x > hinder.x:
                down_hit = True
                up_hit = False

    keys = pg.key.get_pressed() 
    if keys[pg.K_w] and not down_hit:
        mennesket.beveg("opp")
    if keys[pg.K_s] and  not up_hit:
        mennesket.beveg("ned")
    if keys[pg.K_d] and not left_hit:
        mennesket.beveg("høyre")
    if keys[pg.K_a] and not right_hit:
        mennesket.beveg("venstre")

def spøkelse_kontroll(spøkelse, ret, frisone_v, frisone_h):
    spøkelse.endre_retning(frisone_v, frisone_h)
    if ret == "venstre":
        x,y = spøkelse.x, spøkelse.y
        spøkelse.flytt()
    elif ret == "høyre":
        spøkelse.flytt()
    elif ret == "ned":
        spøkelse.flytt()
    elif ret == "opp":
        spøkelse.flytt()
        
        
    
def main():
    start_spøkelse_retning = tilfeldig_retning()
    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    hinderinger = []
    spøkelse = Spøkelse(600,600) #rd.randint(0, SKJERM_BREDDE - 50), rd.randint(0, SKJERM_HØYDE-50))

    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)
    while len(hinderinger) < 3:
        hinder = Hindering(rd.randint(0, SKJERM_BREDDE - 50), rd.randint(0, SKJERM_HØYDE-50))
        hinderinger.append(hinder)
        spille_brett.legg_till_objekt(hinder)

    
    run = True

    while run:
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                sys.exit()
        mennesket_kontroll(menneske, hinderinger)
        #spøkelse_kontroll(spøkelse, start_spøkelse_retning, spille_brett.venstre_frisone, spille_brett.høyre_frisone)
        tegn_viduet(spille_brett)



if __name__ == "__main__":
    main()

    