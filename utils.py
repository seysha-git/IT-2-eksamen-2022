import random as rd
from settings import *
from models import SpilleBrett, SpilleObjekt, Menneske, Spøkelse, Hindering, Sau
import pygame as pg
import sys
import random as rd
def tilfeldig_retning():
    retninger = ["opp", "ned", "høyre", "venstre"]
    return rd.choice(retninger)

def vindu_elementer(vindu, høyre_frisone, venstre_frisone, stolpe):
    pg.draw.rect(vindu, FRISONE_FARGE, venstre_frisone)
    pg.draw.rect(vindu, FRISONE_FARGE,høyre_frisone)
    pg.draw.rect(vindu, STOLPE_FARGE, stolpe)


def tegn_viduet(spille_brett):

    vindu = spille_brett.vindu
    objekter = spille_brett.objekter
    venstre_frisone = spille_brett.venstre_frisone
    høyre_frisone = spille_brett.høyre_frisone
    stolpe = spille_brett.stolpe

    menneske = list(filter(lambda obj: obj.navn == "mennesket", objekter ))[0]
    spøkelser = list(filter(lambda obj: obj.navn == "spøkelse", objekter ))
    spille_brett.vindu.fill("black")
    
    vindu_elementer(vindu, høyre_frisone, venstre_frisone, stolpe)
    mennesket_kontroll(menneske, spille_brett, spøkelser)
    spøkelse_kontroll(spøkelser, venstre_frisone, høyre_frisone)

    for obj in objekter:
        if obj.navn == "hindering":
            hinder = obj
            if hinder.rekt.colliderect(venstre_frisone) or hinder.rekt.colliderect(høyre_frisone):
                print("kolliderte")
                antall_hinderinger -= 1
                objekter.fjern_objekt(hinder)
        if obj.navn == "mennesket":
            mennesket1 = obj 
            if mennesket1.sjekk_kollisjon(høyre_frisone):
                print("Høyre frisone kollisjon")
        obj.plassering(vindu)

        
    
    pg.display.update()



def mennesket_kontroll(mennesket,spille_brett, spøkelser):
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
        if mennesket.sjekk_kollisjon(sau.rekt) and mennesket.bærerSau:
            sys.exit()
        if mennesket.sjekk_kollisjon(sau.rekt):
            spille_brett.fjern_objekt(sau)
            mennesket.bærer_sau()
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
            spøkelse.flytt(-vx, -vy)
        elif spøkelse.ret == "høyre":
            spøkelse.flytt(vx, vy)
        elif spøkelse.ret == "ned":
            spøkelse.flytt(vx,-vy)
        elif spøkelse.ret == "opp":
            spøkelse.flytt(-vx, vy)
        


