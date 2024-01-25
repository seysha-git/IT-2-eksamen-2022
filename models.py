from settings import * 
from utils import *
import pygame as pg 



class SpilleObjekt:
    def __init__(self, xPosisjon:int, yPosisjon:int):
        self.farge =  (0,0,0)
        self.x = xPosisjon
        self.y = yPosisjon
    def flytt(self, int1, int2):
        self.x += int1 
        self.y += int2 
    def plassering(self, int1, int2, vindu):
        rekt = pg.Rect(self.x, self.y, int1, int2)
        pg.draw.rect(vindu, self.farge, rekt)

class SpilleBrett:
    HØYDE_MARGIN = 120
    def __init__(self, bredde:int, høyde:int, farge="black"):
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
   HØYDE,BREDDE = 60,40
   def __init__(self, x,y, fart):
       self.fart = fart
       self.poeng = 0
       self.bærerSau = False 

       self.vx = 0
       self.vy = 0
       super().__init__(x,y)
       self.farge = MENNESKE_FARGE
   def beveg(self, fart, retning):
       self.vx = 0
       self.vy = 0
       if retning == "opp":
         self.vy = -fart
       if retning == "ned":
         self.vy = fart
       if retning == "høyre":
         self.vx = fart
       if retning == "venstre":
         self.vx = -fart
       self.flytt(self.vx, self.vy)

       
    
        

class Spøkelse(SpilleObjekt):
    BREDDE, HØYDE = 30, 30
    def __init__(self, xPosisjon, yPosisjon):
        super().__init__(xPosisjon, yPosisjon)
        self.fart = 2
        self.vx = 2
        self.vy = 2
        self.farge = "green"
    def plassering(self, int1, int2, vindu):
       global rekt
       self.rekt = pg.Rect(self.x, self.y, int1, int2)
       pg.draw.ellipse(vindu, self.farge, self.rekt)
    def endre_retning(self, v, h):
        #if self.rekt.colliderect(v) or self.rekt.colliderect(h):
           # self.vy *= -1
            #self.vx *= -1
        if self.y < 0 or self.y + self.HØYDE + self.fart > SKJERM_HØYDE:
            self.vy *= -1
        if self.x < 0 or self.x + self.BREDDE + self.fart > SKJERM_BREDDE:
            self.vx *= -1
        

class Hindering(SpilleObjekt):
    ... 

class Sau(SpilleObjekt):
    ...


