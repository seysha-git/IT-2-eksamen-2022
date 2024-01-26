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
        self.fart = 4
        self.vx = 4
        self.vy = 4
        self.farge = SPØKELSE_FARGE
    def plassering(self, vindu):
       self.rekt = pg.Rect(self.x, self.y, self.BREDDE, self.HØYDE)
       pg.draw.ellipse(vindu, self.farge, self.rekt)
    def endre_retning(self, v, h):
        dir = rd.choice([-1, 1])
        up_hit, down_hit, left_hit, right_hit = False, False, False,False
        if self.rekt.colliderect(v) or self.rekt.colliderect(h):
            if self.x < FRISONE_BREDDE:
                left_hit = True
                right_hit = False
            if self.x < SKJERM_BREDDE - FRISONE_BREDDE:
                right_hit = True
                left_hit = False
            if self.y > SKJERM_HØYDE//2:
                down_hit = True
                up_hit = False
                print("Oppe treff")
            if self.y < SKJERM_HØYDE//2:
                up_hit = True
                down_hit = False
                print("nede treff")
        #print(self.y, v.y)
        print(up_hit, down_hit, left_hit, right_hit)
        if left_hit or right_hit:
            self.vx *= dir
        if up_hit:
            self.vy *= dir
        if down_hit:
            self.vy *= dir

        

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




