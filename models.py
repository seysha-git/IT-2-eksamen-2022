from settings import * 
from utils import *
import pygame as pg 



class SpilleObjekt:
    BREDDE,HØYDE = 30, 30
    def __init__(self, xPosisjon:int, yPosisjon:int):
        self.y = yPosisjon
        self.x = xPosisjon
        self.farge =  (0,0,0)
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
    def flytt(self, int1, int2):
        self.x += int1
        self.y += int2
    def plassering(self, vindu):
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
        pg.draw.rect(vindu, self.farge, self.rekt)
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
   def __init__(self, x,y):
       self.fart = 5
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
   def sjekk_kollisjon(self):
       ...
            
       

       
    
        

class Spøkelse(SpilleObjekt):
    BREDDE, HØYDE = 45,45
    def __init__(self, xPosisjon, yPosisjon):
        super().__init__(xPosisjon, yPosisjon)
        self.fart = 2
        self.vx = 1
        self.vy = 1
        self.farge = SPØKELSE_FARGE
    def plassering(self, vindu):
       self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
       pg.draw.ellipse(vindu, self.farge, self.rekt)
    def endre_retning(self, v, h):
        #3if self.rekt.colliderect(v) or self.rekt.colliderect(h):
         #   if self.x + self.fart == FRISONE_BREDDE- 3:
         #      self.vx *= -1
          #     print("Høyre frisone vegg kollisjon")
           ####3# self.vy *= -1
        if (self.x >= 0 and self.x <= FRISONE_BREDDE) and (self.y > (SKJERM_HØYDE//2-165) and self.y < ((SKJERM_HØYDE//2-120)+FRISONE_HØYDE)):
            print(self.x, self.y)
            if self.y < SKJERM_HØYDE//2-FRISONE_HØYDE or self.y > SKJERM_HØYDE//1.5-FRISONE_HØYDE:
                self.vy *= -1
                print("top, bunn, venste")
            else:
                print("side venstre")
                self.vx *= -1
        if ((self.x > SKJERM_BREDDE-FRISONE_BREDDE) and (self.x < SKJERM_BREDDE)) and (self.y > (SKJERM_HØYDE//2-165) and self.y < ((SKJERM_HØYDE//2-120)+FRISONE_HØYDE)):
            if self.x + self.vx == SKJERM_BREDDE - FRISONE_BREDDE -50:
              self.vx *= -1
            else:
              self.vy *= -1

        if self.y < 0 or self.y + self.HØYDE + self.fart > SKJERM_HØYDE:
            self.vy *= -1
        if self.x < 0 or self.x + self.BREDDE + self.fart > SKJERM_BREDDE:
            self.vx *= -1
        

class Hindering(SpilleObjekt):
    BREDDE, HØYDE = 60, 60
    def __init__(self, x,y):
        super().__init__(x,y)
        self.farge = HINDER_FARGE
    def plassering(self, vindu):
        self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
        pg.draw.rect(vindu, self.farge, self.rekt)

class Sau(SpilleObjekt):
    ...




