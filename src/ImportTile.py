

import pygame
import os
import Data
#Import Images And Create Rect
screenx = Data.GameWidth
screeny = Data.GameHeight
Screen = pygame.display.set_mode((screenx,screeny))
class ImportImages():
    def __init__(self, ID, Path, ScaleX, ScaleY,PosX=0,PosY=0,Surface=0):
        self.ID = str(ID)
        self.Path = Path
        self.ScaleX = ScaleX
        self.ScaleY = ScaleY
        self.Surface = Surface
        self.PosX = PosX
        self.PosY = PosY
        self.AnimList = []
        self.Name = self.ID
        self.ID = pygame.image.load(self.Path)
        self.ID = pygame.transform.smoothscale(self.ID,(self.ScaleX, self.ScaleY))
   
    def Draw(self, Surface, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        Surface.blit(self.ID, (self.PosX, self.PosY))
    def DrawScale(self, Surface, PosX, PosY,ScaleXA,ScaleYA):
        self.ID = pygame.image.load(self.Path)
        self.ID = pygame.transform.smoothscale(self.ID,(ScaleXA,ScaleYA))
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        Surface.blit(self.ID, (self.PosX, self.PosY))
    def CreateAnimation(self,Patha):
        self.Patha = Patha
        aac = pygame.image.load(self.Patha)
        self.AnimList.append(self.Patha)
    def RunAnim(self,Surface,X,Y):
        for a in self.AnimList:
            aac = pygame.image.load(a)
            Surface.blit(aac,(X,Y))
            pygame.time.delay(25)
    def GoAnim(self,Number,Surface):
        aac = pygame.image.load(self.AnimList[Number])
        Surface.blit(aac,(self.PosX,self.PosY))

dirt = ImportImages("dirt","Data\\Tiles\\Tiles\\Dirt.png",70,70)


grass = ImportImages("grass","Data\\Tiles\\Tiles\\Grass.png",70,70)
sand = ImportImages("sand","Data\\Tiles\\Tiles\\Sand.png",70,70)
water = ImportImages("water","Data\\Tiles\\Tiles\\Water.png",70,70)
dirtmini = ImportImages("dirt","Data\\Tiles\\Tiles\\Dirt.png",1,1)
grassmini = ImportImages("grass","Data\\Tiles\\Tiles\\Grass.png",1,1)
sandmini = ImportImages("sand","Data\\Tiles\\Tiles\\Sand.png",1,1)
watermini = ImportImages("water","Data\\Tiles\\Tiles\\Water.png",1,1)

BackGround = ImportImages("Br","Data\\Tiles\\Tiles\\BackGround.png",1000,700)
ExitIMG = ImportImages("ExitIMG", "Data\\Tiles\\BlockObj\\Exit.png",150,50)
StartIMG = ImportImages("StartIMG", "Data\\Tiles\\BlockObj\\Start.png",150,50)
MenuIMG = ImportImages("MenuIMG", "Data\\Tiles\\BlockObj\\Menu.png",150,50)
HouseSl = ImportImages("HouseSl", "Data\\Tiles\\BlockObj\\HouseB.png",50,50)
House = ImportImages("House","Data\\Tiles\\Tiles\\House.png",50,50)





Player = ImportImages("MenuIMG", "Data\\Tiles\\Tiles\\PlayerF.png",150,50,100,100,Screen)
Player.CreateAnimation("Data\\Tiles\\Tiles\\PlayerR.png")
Player.CreateAnimation("Data\\Tiles\\Tiles\\PlayerL.png")