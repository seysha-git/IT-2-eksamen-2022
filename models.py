from settings import * 
from utils import *
import pygame as pg 



class SpilleObjekt:
    """
    Tlpasset egenskaper:
    self.navn: Lar meg identifisere objektene i SpilleBrettet
    self.farge = En RGB-farge (Se settings) for objektene slik at de er visuelt forskjellig
    self.rekt = Lar meg bruke figuren i andre metoder, f.eks sjekkKoollisjon i mennesketObjekt

    Tilpasset metoder:
    plassering(vindu): Fjerna x,y kordinat som parameter fordi allerede definert i konstruktør.
                       La til vindu som parameter, nødvendig for tegning på skjermen
    
    """
    BREDDE,HØYDE = 30, 30
    def __init__(self, xPosisjon:int, yPosisjon:int):
        self.name = "objekt"
        self.y = yPosisjon
        self.x = xPosisjon
        self.farge =  (0,0,0)
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
    def flytt(self, int1, int2):
        self.x = int1
        self.y = int2
    def plassering(self, vindu):
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
        pg.draw.rect(vindu, self.farge, self.rekt)
class SpilleBrett:
    """
    Tilpasset egenskaper:
    self.vindu: Lager skjermen i spillebrettet
    self.venstre_frsione, self.høyre_frisone: Lager begge frisonene i klassen
    self.stolpe: Et skille i midten bare for design skyld



    
    
    """
    HØYDE_MARGIN = 120
    def __init__(self, bredde:int, høyde:int):
        self.vindu = pg.display.set_mode((bredde, høyde))
        self.venstre_frisone = pg.Rect(0, SKJERM_HØYDE//2-self.HØYDE_MARGIN, FRISONE_BREDDE, FRISONE_HØYDE)
        self.høyre_frisone = pg.Rect(bredde-FRISONE_BREDDE, SKJERM_HØYDE//2 - self.HØYDE_MARGIN, FRISONE_BREDDE, FRISONE_HØYDE)
        self.stolpe = pg.Rect(bredde//2 - STOLPE_BREDDE, 0, STOLPE_BREDDE, høyde)
        
        self.objekter = []
    def legg_till_objekt(self, objekt):
        self.objekter.append(objekt)
    def fjern_objekt(self, objekt):
        self.objekter.remove(objekt)
class Menneske(SpilleObjekt):
   """
   Tlpasset egenskaper:
   self.vx, self.vy: Lar meg kontrollere farten i x og y retning
   Tilpasset metoder:
   sjekk_kollisjon(andreObjekt): Nødvendig med annet objekt for å sjekke kollisjon
   
   """
   HØYDE,BREDDE = 60,40
   def __init__(self, x,y):
       self.navn = "mennesket"
       self.fart = 7
       self.poeng = 0
       self.bærerSau = False 
       self.vx = 0
       self.vy = 0
       super().__init__(x,y)
       self.farge = MENNESKE_FARGE
   def flytt(self, int1, int2):
        self.x += int1
        self.y += int2
   def beveg(self, retning):
       self.vx = 0
       self.vy = 0
       if retning == "opp":
         self.vy = -self.fart
       if retning == "ned":
         self.vy = self.fart
       if retning == "høyre":
         self.vx = self.fart
       if retning == "venstre":
         self.vx = -self.fart
       self.flytt(self.vx, self.vy)
   def reduser_fart(self):
       self.fart = 5
   def øk_poeng(self):
       self.poeng += 1
   def sjekk_kollisjon(self, andre_objekt):
       return self.rekt.colliderect(andre_objekt)
            
       

       
    
        

class Spøkelse(SpilleObjekt):
    """
    Tilpasset egenskaper:
    self.vx, self.vy: Lar meg kontrollere farten i x og y retning
    self.ret = start_retningen som spøkelse beveger i

    Tilpasset metoder:
    endre_retning(): Trennger venstre, høyre frisone for å finne kolisjonen hvor den endrer retning
    """
    BREDDE, HØYDE = 45,45
    def __init__(self, ret):
        self.x = rd.randint(200, SKJERM_BREDDE-FRISONE_BREDDE-100)
        self.y = rd.randint(0, SKJERM_HØYDE-50, )
        super().__init__(self.x, self.y)
        self.navn = "spøkelse"
        self.fart = 4
        self.vx = 4
        self.vy = 4
        self.farge = SPØKELSE_FARGE
        self.ret = ret
    def plassering(self, vindu):
       self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
       pg.draw.ellipse(vindu, self.farge, self.rekt)
    def endre_retning(self, v, h):
        up_hit, down_hit, left_hit, right_hit = False, False, False,False
        if self.rekt.colliderect(v) or self.rekt.colliderect(h):
            if self.x < FRISONE_BREDDE:
                left_hit = True
                right_hit = False
            if self.x < SKJERM_BREDDE - FRISONE_BREDDE:
                right_hit = True
                left_hit = False
            if self.y > SKJERM_HØYDE//2 + FRISONE_HØYDE//4:
                down_hit = True
            if self.y < SKJERM_HØYDE//2 - FRISONE_HØYDE // 2:
                up_hit = True
        if left_hit or right_hit:
            dir = rd.choice([-1, 1])
            self.vx *= -1
        if up_hit or down_hit:
            dir = rd.choice([-1, 1])
            self.vy *= -1

        if self.y < 0 or self.y + self.HØYDE + self.fart > SKJERM_HØYDE:
            self.vy *= -1
        if self.x < 0 or self.x + self.BREDDE + self.fart > SKJERM_BREDDE:
            self.vx *= -1
        

class Hindering(SpilleObjekt):
    BREDDE, HØYDE = 60, 60
    def __init__(self):
        self.x =  rd.randint(0, SKJERM_BREDDE - 50)
        self.y = rd.randint(0, SKJERM_HØYDE-50)
        super().__init__(self.x, self.y)
        self.navn = "hindering"
        self.farge = HINDER_FARGE

class Sau(SpilleObjekt):
    BREDDE,HØYDE = 40, 20
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__(x,y)
        self.navn = "sau"
        self.farge = SAU_FARGE
        self.blir_båret = False
    def plassering(self, vindu):
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
        pg.draw.rect(vindu, self.farge, self.rekt)
        
    def blir_løftet(self):
        self.blir_båret = True
        self.fjern_sau()
    def fjern_sau(self):
        ...
        
        
    
    
    




