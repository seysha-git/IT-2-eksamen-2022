from settings import * 
from utils import *
import pygame as pg 



class SpilleObjekt:
    def __init__(self, xPosisjon:int, yPosisjon:int, bredde:int, høyde:int, farge:str):
        self.farge = farge

        self.x = xPosisjon
        self.y = yPosisjon
        self.vx = 0
        self.vy = 0

        self.bredde = bredde
        self.høyde = høyde

    def flytt(self, int1, int2):
        self.x = int1 
        self.y = int2
    def plassering(self,vindu, int1, int2):
        rect = pg.Rect(int1, int2, self.bredde, self.høyde)
        pg.draw.rect(vindu,self.farge, rect)


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
    def __init__(self, xPosisjon, yPosisjon, bredde, høyde, farge, poeng):
        self.fart = 5
        self.poeng = poeng
        super().__init__(xPosisjon, yPosisjon, bredde, høyde, farge)
    def beveg(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        

class Spøkelse(SpilleObjekt):
    ...

class Hindering(SpilleObjekt):
    ... 

class Sau(SpilleObjekt):
    ...


