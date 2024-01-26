from models import * 
from settings import * 
from utils import *
import sys
import random as rd

def vinduet_design(vindu, spille_brett):
    pg.draw.rect(vindu, FRISONE_FARGE, spille_brett.venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,spille_brett.høyre_frisone)
    pg.draw.rect(spille_brett.vindu, STOLPE_FARGE, spille_brett.stolpe)


def tegn_viduet(spille_brett):
    vindu = spille_brett.vindu
    objekter = spille_brett.objekter
    venstre_frisone = spille_brett.venstre_frisone
    høyre_frisone = spille_brett.høyre_frisone
    menneske = list(filter(lambda obj: obj.navn == "mennesket", objekter ))[0]
    spøkelser = list(filter(lambda obj: obj.navn == "spøkelse", objekter ))
    spille_brett.vindu.fill("black")
    
    vinduet_design(vindu, spille_brett)
    mennesket_kontroll(menneske, spille_brett)
    spøkelse_kontroll(spøkelser, "venstre", venstre_frisone, høyre_frisone)

    for obj in spille_brett.objekter:
        obj.plassering(vindu)

        
    

    pg.display.update()



def mennesket_kontroll(mennesket,spille_brett):
    up_hit, down_hit, left_hit, right_hit = False, False, False, False
    hinderinger = list(filter(lambda obj: obj.navn == "hindering", spille_brett.objekter))

    for hinder in hinderinger:
        if mennesket.rekt.colliderect(hinder.rekt):
            if hinder.x > mennesket.x:
                left_hit = True
                right_hit = False
            elif mennesket.x > hinder.x:
                right_hit = True
                left_hit = False
            if hinder.y > mennesket.y:
                up_hit = True
                down_hit = False
            elif mennesket.y > hinder.y:
                down_hit = True
                up_hit = False

    keys = pg.key.get_pressed() 
    if keys[pg.K_w] and not down_hit and mennesket.y > 0:
        mennesket.beveg("opp")
    if keys[pg.K_s] and  not up_hit and mennesket.y + mennesket.fart + mennesket.HØYDE < SKJERM_HØYDE:
        mennesket.beveg("ned")
    if keys[pg.K_d] and not left_hit and mennesket.x + mennesket.BREDDE + mennesket.fart< SKJERM_BREDDE:
        mennesket.beveg("høyre")
    if keys[pg.K_a] and not right_hit and mennesket.x > 0:
        mennesket.beveg("venstre")
    
    sauer = list(filter(lambda obj: obj.navn == "sau", spille_brett.objekter))
    for sau in sauer:
        if mennesket.sjekk_kollisjon(sau.rekt):
            spille_brett.fjern_objekt(sau)
            mennesket.bærer_sau()
            mennesket.reduser_fart()
    if mennesket.sjekk_kollisjon(spille_brett.venstre_frisone) and mennesket.bærerSau:
        print("Slipp Sau")
        spille_brett.legg_till_objekt(Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
        spille_brett.legg_till_objekt(Spøkelse(rd.randint(200, SKJERM_BREDDE-200), rd.randint(0, SKJERM_HØYDE-50)))
        spille_brett.legg_till_objekt(Hindering(rd.randint(0, SKJERM_BREDDE - 50), rd.randint(0, SKJERM_HØYDE-50)))
        mennesket.bærerSau = False





    

def spøkelse_kontroll(spøkelser, ret, frisone_v, frisone_h):
    for spøkelse in spøkelser:
        spøkelse.endre_retning(frisone_v, frisone_h)
        vx,vy = spøkelse.vx, spøkelse.vy
        if ret == "venstre":
            spøkelse.flytt(-vx, -vy)
        elif ret == "høyre":
            spøkelse.flytt(vx, vy)
        elif ret == "ned":
            spøkelse.flytt(vx,-vy)
        elif ret == "opp":
            spøkelse.flytt(-vx, vy)
        
        
    
def main():
    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    antall_hinderinger = 3
    antall_sauer = 3
    antal_spøkelser = 1
    spøkelse = Spøkelse(rd.randint(200, SKJERM_BREDDE-200), rd.randint(0, SKJERM_HØYDE-50))

    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)

    run = True
    while run:
        clock.tick(FPS)
        while antall_hinderinger > 0:
            ikke_kollidert = False
            while not ikke_kollidert:
                x,y = rd.randint(0, SKJERM_BREDDE - 50), rd.randint(0, SKJERM_HØYDE-50)
                hinder = Hindering(x,y)
                ikke_kollidert = True
                if hinder.rekt.colliderect(spille_brett.venstre_frisone) or hinder.rekt.colliderect(spille_brett.høyre_frisone):
                    print("kolliderte")
                    ikke_kollidert = False
            spille_brett.legg_till_objekt(hinder)
            antall_hinderinger -= 1
        while antall_sauer > 0:
            ikke_kollidert_sau = False
            while not ikke_kollidert_sau:
                x,y = rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)
                ny_sau = Sau(x,y)
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



