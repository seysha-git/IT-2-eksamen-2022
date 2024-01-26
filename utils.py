import random as rd
from settings import *
import pygame as pg
def tilfeldig_retning():
    retninger = ["opp", "ned", "høyre", "venstre"]
    return "opp" #rd.choice(retninger)

def sjekk_start_kollision(hinderinger, venstre_frisone, høyre_frisone):
    for i in range(len(hinderinger)):
        if hinderinger[i].rekt.colliderect(venstre_frisone) or hinderinger[i].rekt.colliderect(høyre_frisone):
          hinderinger.remove(hinderinger[i])
          print("flyttet den")


