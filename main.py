from settings import * 
from utils import *
import sys
import random as rd

def tegn_vinduet(spille_brett):
    spille_brett.vindu.fill("black")
    vindu = spille_brett.vindu
    objekter = spille_brett.objekter
    venstre_frisone = spille_brett.venstre_frisone
    høyre_frisone = spille_brett.høyre_frisone
    stolpe = spille_brett.stolpe

    pg.draw.rect(vindu, FRISONE_FARGE, venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,høyre_frisone)
    pg.draw.rect(vindu, STOLPE_FARGE, stolpe)

    menneske = hent_objekter(objekter, "mennesket")[0]
    spøkelser = hent_objekter(objekter, "spøkelse")

    
    mennesket_kontroll(menneske, spille_brett, spøkelser)
    spøkelse_kontroll(spøkelser, venstre_frisone, høyre_frisone)

    for obj in objekter:
        if obj.navn == "hindering":
            hinder = obj
            hinderinger = hent_objekter(objekter, "hindering")
            if hinder.rekt.colliderect(venstre_frisone) or hinder.rekt.colliderect(høyre_frisone):
                print("Hinder kolliderte med rektangel, men ble så flyttet")
                spille_brett.fjern_objekt(hinder)
                spille_brett.legg_till_objekt(Hindering())
            if sjekk_innen_kollisjon(hinder, hinderinger, False):
                spille_brett.fjern_objekt(obj)
                spille_brett.legg_till_objekt(Hindering())

        if obj.navn == "sau":
            sauer = hent_objekter(objekter, "sau")
            sau = obj
            if sjekk_innen_kollisjon(sau, sauer, False):
                if sau.rekt.colliderect(venstre_frisone):
                    spille_brett.fjern_objekt(sau)
                    spille_brett.legg_till_objekt(Sau(rd.randint(0, FRISONE_BREDDE-100), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
                if sau.rekt.colliderect(høyre_frisone):
                    spille_brett.fjern_objekt(sau)
                    spille_brett.legg_till_objekt(Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
                
                                    
        obj.plassering(vindu)
    pg.display.update()


def mennesket_kontroll(mennesket,spille_brett, spøkelser):
    up_hit, down_hit, left_hit, right_hit = False, False, False, False
    hinderinger = hent_objekter(spille_brett.objekter, "hindering")

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
    
    sauer = hent_objekter(spille_brett.objekter, "sau")
    for sau in sauer:
        if mennesket.sjekk_kollisjon(sau.rekt) and mennesket.bærerSau:
            sys.exit()
        if mennesket.sjekk_kollisjon(sau.rekt) and mennesket.sjekk_kollisjon(spille_brett.høyre_frisone):
            spille_brett.fjern_objekt(sau)
            mennesket.bærerSau = True
            mennesket.reduser_fart()

    if mennesket.sjekk_kollisjon(spille_brett.venstre_frisone) and mennesket.bærerSau:
        mennesket.fart = 5
        spille_brett.legg_till_objekt(Sau(rd.randint(0, FRISONE_BREDDE-100), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
        spille_brett.legg_till_objekt(Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
        spille_brett.legg_till_objekt(Spøkelse(tilfeldig_retning()))
        spille_brett.legg_till_objekt(Hindering())
        mennesket.bærerSau = False
    
    for spøkelse in spøkelser:
        if mennesket.sjekk_kollisjon(spøkelse.rekt):
            sys.exit()

def spøkelse_kontroll(spøkelser, frisone_v, frisone_h):
    for spøkelse in spøkelser:
        spøkelse.endre_retning(frisone_v, frisone_h)
        vx,vy = spøkelse.vx, spøkelse.vy
        if spøkelse.ret == "venstre":
            spøkelse.flytt(spøkelse.x-vx, spøkelse.y-vy)
        elif spøkelse.ret == "høyre":
            spøkelse.flytt(spøkelse.x+vx, spøkelse.y+vy)
        elif spøkelse.ret == "ned":
            spøkelse.flytt(spøkelse.x+vx,spøkelse.y-vy)
        elif spøkelse.ret == "opp":
            spøkelse.flytt(spøkelse.x-vx,spøkelse.y+vy)
        





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



