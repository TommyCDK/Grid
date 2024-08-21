

import pygame
import os
#Import Images And Create Rect

class ImportImages():
    def __init__(self, ID, Path, ScaleX, ScaleY):
        self.ID = str(ID)
        self.Path = Path
        self.ScaleX = ScaleX
        self.ScaleY = ScaleY
        
    def Install(self):
        self.Name = self.ID
        self.ID = pygame.image.load(self.Path)
        self.ID = pygame.transform.smoothscale(self.ID,(self.ScaleX, self.ScaleY))
    
    def Draw(self, Surface, PosX, PosY):
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        Surface.blit(self.ID, (self.PosX, self.PosY))

dirt = ImportImages("dirt","Data\\Tiles\\Tiles\\Dirt.png",100,70)
dirt.Install()

grass = ImportImages("grass","Data\\Tiles\\Tiles\\Grass.png",100,70)
grass.Install()

sand = ImportImages("sand","Data\\Tiles\\Tiles\\Sand.png",100,70)
sand.Install()

water = ImportImages("water","Data\\Tiles\\Tiles\\Water.png",100,70)
water.Install()

dirtmini = ImportImages("dirt","Data\\Tiles\\Tiles\\Dirt.png",1,1)
dirtmini.Install()

grassmini = ImportImages("grass","Data\\Tiles\\Tiles\\Grass.png",1,1)
grassmini.Install()

sandmini = ImportImages("sand","Data\\Tiles\\Tiles\\Sand.png",1,1)
sandmini.Install()

watermini = ImportImages("water","Data\\Tiles\\Tiles\\Water.png",1,1)
watermini.Install()

ExitIMG = ImportImages("ExitIMG", "Data\\Tiles\\BlockObj\\Exit.png",150,50)
ExitIMG.Install()

StartIMG = ImportImages("StartIMG", "Data\\Tiles\\BlockObj\\Start.png",150,50)
StartIMG.Install()

MenuIMG = ImportImages("MenuIMG", "Data\\Tiles\\BlockObj\\Menu.png",150,50)
MenuIMG.Install()