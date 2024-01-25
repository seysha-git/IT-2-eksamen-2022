from settings import * 
from utils import *
import pygame as pg 



class SpilleObjekt:
    def __init__(self, xPosisjon:int, yPosisjon:int):
        self.x = xPosisjon
        self.y = yPosisjon
    def flytt(self, int1, int2):
        self.x += int1 
        self.y += int2 
    def plassering(self, int1, int2, vindu):
        rekt = pg.Rect(self.x, self.y, int1, int2)
        pg.draw.rect(vindu, "grey", rekt)

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
   def __init__(self, x,y, fart):
       self.fart = fart
       self.poeng = 0
       self.bærerSau = False 

       self.vx = 0
       self.vy = 0
       super().__init__(x,y)
   def plassering(self, int1, int2, vindu):
       rekt = pg.Rect(self.x, self.y, int1, int2)
       pg.draw.rect(vindu, "blue", rekt)
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
    ...

class Hindering(SpilleObjekt):
    ... 

class Sau(SpilleObjekt):
    ...


