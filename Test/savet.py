
import pygame

from pygame.locals import *
import sys
import ctypes
import time
import Draw as D
import ImportTile as IP
import Data
screenx = Data.GameWidth
screeny = Data.GameHeight
screen = pygame.display.set_mode((screenx,screeny))









House = IP.HouseSl
HouseButt = D.CreateButtonImages(House, 1010,50,screen)
ExitImage = IP.ExitIMG
ExitButton = D.CreateButtonImages(ExitImage,400,520,screen)


def NoneExcute():
    print('None')
def exitgame():
    pygame.quit()
    sys.exit()

def Viller():
    HouseButt.DrawScale(NoneExcute,50,50)


def Listenevent(): #Screen 1
    if Data.Sc1ForViler:
        Viller()
    else: pass
    pass
