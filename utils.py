import random as rd
from settings import *
from models import SpilleBrett, SpilleObjekt, Menneske, Spøkelse, Hindering, Sau
import pygame as pg
import sys
import random as rd

def hent_objekter(objekter, navn):
    return [obj for obj in objekter if obj.navn == navn]

def sjekk_innen_kollisjon(obj, objs, bool):
        bool = False
        for i in range(len(objs)):
            if obj == objs[i]:
                for j in range(i+1, len(objs)):
                    if obj.rekt.colliderect(objs[j].rekt):
                        obj.farge = "black"
                        bool = True
        return bool

def tilfeldig_retning():
    retninger = ["opp", "ned", "høyre", "venstre"]
    return rd.choice(retninger)



    
    

   

