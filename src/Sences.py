
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


s1 = False






StartImage = IP.StartIMG
StartButton = D.CreateButtonImages(StartImage, 400,450,screen)
ExitImage = IP.ExitIMG
ExitButton = D.CreateButtonImages(ExitImage,400,520,screen)
def test():
    print("opoppopoopopopoppo")   

def NoneExcute():
    pass
def exitgame():
    pygame.quit()
    sys.exit()




def sc1(): #Screen 1
    
    pass
