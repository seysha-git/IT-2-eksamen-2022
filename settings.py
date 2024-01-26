import pygame as pg
import os
pg.font.init()

#Screen settings 
SKJERM_HØYDE, SKJERM_BREDDE = 800,1300
FRISONE_HØYDE, FRISONE_BREDDE = 200, 200

STOLPE_BREDDE = 20
pg.display.set_caption("Manic Mansion")

#vinduet
WIN = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HØYDE))

#FOnts
START_FONT = pg.font.SysFont("comicsans", 40)
FINISHED_FONT = pg.font.SysFont("comicsans", 40)
POINTS_FONT = pg.font.SysFont("comicsans", 40)

#Other
FPS = 60
clock = pg.time.Clock()
#colors
MENNESKE_FARGE = (134, 166, 215)
SAU_FARGE = (245, 240, 240)
HINDER_FARGE = (236, 168, 36)
SPØKELSE_FARGE = (107, 111, 113)
FRISONE_FARGE = (217,217, 217)
STOLPE_FARGE = (35, 37,38)