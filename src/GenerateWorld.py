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

  


Screen.fill(ScreenFill)

asdds= D.HoldDragMouse((0,255,0),3,Screen)

clock = pygame.time.Clock()

def Nonee():
    print("asdasdasd")


while run:
    Screen.fill(ScreenFill)
    pygame.draw.line(Screen,(15,100,150),(1001,0),(1001,700),(5))
    Sences.Listenevent()
    delta_time = clock.get_time() / 1000.0
    IP.BackGround.Draw(Screen,0,0)
    D.p.LoadProp()
    D.p.Move(delta_time)
    asdds.Run()
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            Data.OnOff()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    






    

    clock.tick(60)
    pygame.display.flip()

quit()