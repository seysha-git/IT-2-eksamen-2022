from settings import * 
from utils import *
from models import *
import sys
import random as rd

def tegn_vinduet(spille_brett, menneske):
    spille_brett.vindu.fill("black")

    pg.draw.rect(spille_brett.vindu, FRISONE_FARGE, spille_brett.venstre_frisone)
    pg.draw.rect(spille_brett.vindu, FRISONE_FARGE,spille_brett.høyre_frisone)
    pg.draw.rect(spille_brett.vindu, STOLPE_FARGE, spille_brett.stolpe)


    if menneske.sjekk_kollisjon(spille_brett.venstre_frisone) and menneske.bærerSau:
        menneske.endre_fart(7) 
        menneske.bær_sau(False)
        menneske.øk_poeng()

        spille_brett.legg_till_objekt(Sau(rd.randint(0, FRISONE_BREDDE-100), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
        spille_brett.legg_till_objekt(Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
        spille_brett.legg_till_objekt(Spøkelse(tilfeldig_retning()))
        spille_brett.legg_till_objekt(Hindering())

    for obj in spille_brett.objekter:
        if obj.navn == "hindering":
            hinder = obj
            hinderinger = hent_objekter(spille_brett.objekter, "hindering")
            if hinder.rekt.colliderect(spille_brett.venstre_frisone) or hinder.rekt.colliderect(spille_brett.høyre_frisone):
                spille_brett.fjern_objekt(hinder)
                spille_brett.legg_till_objekt(Hindering())
            if sjekk_innen_kollisjon(hinder, hinderinger, False):
                spille_brett.fjern_objekt(obj)
                spille_brett.legg_till_objekt(Hindering())
        if obj.navn == "spøkelse":
            if menneske.sjekk_kollisjon(obj.rekt):
                avslutt_spill()
        if obj.navn == "sau":
            sauer = hent_objekter(spille_brett.objekter, "sau")
            if menneske.sjekk_kollisjon(obj.rekt) and menneske.bærerSau:
                avslutt_spill()
            if menneske.sjekk_kollisjon(obj.rekt) and menneske.sjekk_kollisjon(spille_brett.høyre_frisone):
                menneske.bær_sau(True)
                menneske.endre_fart(3.5)
                spille_brett.fjern_objekt(obj)
            if sjekk_innen_kollisjon(obj, sauer, False):
                if obj.rekt.colliderect(spille_brett.venstre_frisone):
                    spille_brett.fjern_objekt(obj)
                    spille_brett.legg_till_objekt(Sau(rd.randint(0, FRISONE_BREDDE-100), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
                if obj.rekt.colliderect(spille_brett.høyre_frisone):
                    spille_brett.fjern_objekt(obj)
                    spille_brett.legg_till_objekt(Sau(rd.randint(SKJERM_BREDDE-FRISONE_BREDDE, SKJERM_BREDDE-FRISONE_BREDDE//8), rd.randint(SKJERM_HØYDE//2 - 120, (SKJERM_HØYDE//2 - 120)+ FRISONE_HØYDE-50)))
                
                                    
        obj.plassering(spille_brett.vindu)
    pg.display.update()


def mennesket_kontroll(mennesket, hinderinger):
    up_hit, down_hit, left_hit, right_hit = False, False, False, False

    for hinder in hinderinger:
        if mennesket.sjekk_kollisjon(hinder.rekt):
            if hinder.x > mennesket.x:
                left_hit, right_hit = True, False
            elif mennesket.x > hinder.x:
                right_hit, left_hit = True, False
            if hinder.y > mennesket.y:
                up_hit, down_hit = True, False
            elif mennesket.y > hinder.y:
                down_hit, up_hit = True, False

    keys = pg.key.get_pressed() 
    if keys[pg.K_w] and not down_hit and mennesket.y > 0:
        mennesket.beveg("opp")
    if keys[pg.K_s] and  not up_hit and mennesket.y + mennesket.fart + mennesket.HØYDE < SKJERM_HØYDE:
        mennesket.beveg("ned")
    if keys[pg.K_d] and not left_hit and mennesket.x + mennesket.BREDDE + mennesket.fart< SKJERM_BREDDE:
        mennesket.beveg("høyre")
    if keys[pg.K_a] and not right_hit and mennesket.x > 0:
        mennesket.beveg("venstre")
    

    
def spøkelse_kontroll(spøkelser, frisone_v, frisone_h):
    for spøkelse in spøkelser:
        spøkelse.endre_retning(frisone_v, frisone_h)
        vx,vy = spøkelse.vx, spøkelse.vy
        if spøkelse.ret == "venstre":
            spøkelse.flytt(-vx, -vy)
        elif spøkelse.ret == "høyre":
            spøkelse.flytt(vx, vy)
        elif spøkelse.ret == "ned":
            spøkelse.flytt(vx,-vy)
        elif spøkelse.ret == "opp":
            spøkelse.flytt(-vx,vy)
        

def main():
    """
    Implementerer: ¨
        Ved oppstart skal spillet bestå av:
             Spillebrett, 
             Menneskeobjekt
             Spøkelsesobjekt
             Tre hindringsobjekter 
             Tre saueobjekter
        Det er gjort før  spillet begynner
    """
    antall_start_hinderinger = 0
    antall_start_sauer = 0

    spille_brett = SpilleBrett(SKJERM_BREDDE, SKJERM_HØYDE)
    menneske = Menneske(50, SKJERM_HØYDE//2-100)
    spøkelse = Spøkelse(tilfeldig_retning())

    spille_brett.legg_till_objekt(menneske)
    spille_brett.legg_till_objekt(spøkelse)

    while antall_start_hinderinger < 3:
        ikke_kollidert = False
        #Ingen objekter skal være oppå hverandre.
        while not ikke_kollidert:
            ny_hinder = Hindering()
            ikke_kollidert = True
            if ny_hinder.rekt.colliderect(spøkelse.rekt):
                ikke_kollidert = False
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
                avslutt_spill()
    
        menneske = hent_objekter(spille_brett.objekter, "mennesket")[0]
        spøkelser = hent_objekter(spille_brett.objekter, "spøkelse")
        hinderinger = hent_objekter(spille_brett.objekter, "hindering")


        mennesket_kontroll(menneske,  hinderinger) # Menneskeobjekt piltast kontroller
        spøkelse_kontroll(spøkelser, spille_brett.venstre_frisone, spille_brett.høyre_frisone) # Spøkelse tilfeldig bevegelse
        tegn_vinduet(spille_brett, menneske)
        #
if __name__ == "__main__":
    main()



