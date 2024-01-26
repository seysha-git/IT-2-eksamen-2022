import random as rd
from settings import *
import pygame as pg
def tilfeldig_retning():
    retninger = ["opp", "ned", "høyre", "venstre"]
    return rd.choice(retninger)

