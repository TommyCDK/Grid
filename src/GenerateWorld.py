import pygame

from pygame.locals import *
import sys
import ctypes
import time
import Draw as D
import ImportTile as IP
import Sences
import Data
pygame.init()





#Screen Settings
screenx = Data.GameWidth
screeny = Data.GameHeight
ScreenFill = Data.GameFill
Screen = pygame.display.set_mode((screenx,screeny))

run = True





fc = False

def fcc(): #FullScreen Toggle

    if fc == True:

        ctypes.windll.user32.SetProcessDPIAware()

        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        pygame.display.set_mode(true_res,pygame.FULLSCREEN)

    else:

        screen = pygame.display.set_mode((1000,720))

Map = D.loadmap("Map1",Screen)   
Map.LoadTile()  

a = D.GenMap(10,10)
a.gen("Map1")                   
def RunModule():
    
    if Sences.s1: Sences.sc1()
    pass

player = D.Player(100,50,200,200)
Screen.fill(ScreenFill)
while run:
    Screen.fill(ScreenFill)
    Map.UpdateMoving()
    Map.DrawTile()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    RunModule()





    


    pygame.display.flip()

quit()