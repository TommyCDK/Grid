


import pygame
import sys
from pygame import *
import random 
import os
import ImportTile
import Data
screenx = Data.GameWidth
screeny = Data.GameHeight

 
screen = pygame.display.set_mode((screenx,screeny))
class slot(): #Draw Square With OutLine

        def __init__(self, LineColor, BackgroundColor, ScaleX, ScaleY, LineWidth, PosX, PosY):

            self.LineColor =  LineColor
            self.LineWidth = LineWidth
            self.BackgroundColor = BackgroundColor
            self.ScaleX = ScaleX
            self.ScaleY = ScaleY
            self.PosX = PosX
            self.PosY  = PosY        
            LineWidth = int(LineWidth)
            RectName = Rect((PosX,PosY),(ScaleX,ScaleY))
        def Draw(self, Surface):
            self.Surface = Surface
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY),(self.PosX+self.ScaleX,self.PosY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY),(self.PosX,self.PosY+self.ScaleY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX+self.ScaleX,self.PosY),(self.PosX+self.ScaleX,self.PosY+self.ScaleY),self.LineWidth)
            pygame.draw.line(Surface,self.LineColor,(self.PosX,self.PosY+self.ScaleY),(self.PosX+self.ScaleX,self.PosY+self.ScaleY),self.LineWidth)







class CreateButtonSlot():
        
    def __init__(self, Rect, Surface): #Import Rect
        self.Rect = Rect 
        self.rectx = self.Rect.PosX
        self.recty = self.Rect.PosY
        self.rectscaleX = self.Rect.ScaleX
        self.rectscaleY = self.Rect.ScaleY
        LineWidth = self.Rect.LineWidth
        LineColor = self.Rect.LineColor 
        self.CheckClick = False 
        self.IsHover = False
        self.Surface = Surface
    def Draw(self, Execute):  #Check Click
        self.Rect.draw(self.Surface)
        self.Execute = Execute 
        self.but = Rect((self.rectx,self.recty),(self.rectscaleX,self.rectscaleY))
        if self.but.collidepoint(pygame.mouse.get_pos()) :
            if pygame.mouse.get_pressed()[0] and not self.CheckClick:
                self.CheckClick = True
                Execute()
            if not pygame.mouse.get_pressed()[0]:
                self.CheckClick = False

class CreateButtonImages():
    def __init__(self, Images, PosX, PosY, Surface):
        self.Images = Images
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        self.ImageScaleX = self.Images.ScaleX
        self.ImageScaleY = self.Images.ScaleY
        self.ImageHitBox = Rect(self.PosX, self.PosY, self.ImageScaleX, self.ImageScaleY)
        self.CheckClick = False
    def Draw(self, Execute):
        self.Execute = Execute
        self.Images.Draw(self.Surface,self.PosX,self.PosY)
        if self.ImageHitBox.collidepoint(pygame.mouse.get_pos()) :
            if pygame.mouse.get_pressed()[0] and not self.CheckClick:
                self.CheckClick = True
                Execute()
            if not pygame.mouse.get_pressed()[0]:
                self.CheckClick = False

    def draw(self,screen):
        screen.blit(screen,self.Images,(self.PosX,self.PosY))


def fcc(): #FullScreen Toggle

    if fc == True:

        ctypes.windll.user32.SetProcessDPIAware()

        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        pygame.display.set_mode(true_res,pygame.FULLSCREEN)

    else:

        screen = pygame.display.set_mode((1000,720))

class Player():
    def __init__(self, Health, Speed, PosX, PosY):
        self.Health = Health
        self.Speed = Speed
        self.PosX = PosX
        self.PosY = PosY
    def Spawn(self):
        self.Rect = Rect(self.PosX, self.PosY, 50,50)
        pygame.draw.rect(screen,"green",self.Rect)
    def Move(self, X, Y):
        self.playerx = self.PosX
        self.playery = self.PosY
        X = int(X)
        y = int(Y)
        self.k = pygame.key.get_pressed()
        k = self.k
    
        if k[pygame.K_w ]:
            
            if k[pygame.K_a ]:
                if self.playery >= 150:
                    self.PosY -= Y/1.5
                    self.PosX -= X/1.5
            elif k[pygame.K_d ]:
                if self.playery >= 150:
                    self.PosY -= Y/1.5 
                    self.PosX += X/1.5
        if k[pygame.K_s ]:
            if k[pygame.K_a ]:
                self.PosY += Y/1.5
                self.PosX -= X/1.5
            elif k[pygame.K_d ]:
                self.PosY += Y/1.5 
                self.PosX += X/1.5
        if k[pygame.K_w ] and k[pygame.K_a] == False and k[pygame.K_d]  == False:
            if self.playery >= 150:
                self.PosY -= Y       
        if k[pygame.K_s] and k[pygame.K_a] == False and k[pygame.K_d]  == False:
            self.PosY += Y
        if k[pygame.K_a] and k[pygame.K_w] == False and k[pygame.K_s]  == False:
            self.PosX -= X
        if k[pygame.K_d] and k[pygame.K_w] == False and k[pygame.K_s]  == False:
            self.PosX += X
        pygame.time.delay(50) 
    def shoot(self):
        k = self.k
        a = self.PosX + 20
        x = self.PosY + 15
        if k[pygame.K_SPACE]:
            while x > 100:
                Bull = Rect(a, x, 10, 10)
                pygame.draw.rect(screen,"red",Bull)
                x -= 10


class GenMap():
    def __init__(self, BlockPerChunk, ChunkRange):
        self.BlockPerChunk = BlockPerChunk
        BlockPerChunk = int(BlockPerChunk)
        self.ChunkRange = ChunkRange
    def gen(self, MapID):
        self.MapID = MapID
        self.MapPath = "Data\\Game\\Maps\\" + str(MapID) + ".txt"
        BlockPerChunk = int(self.BlockPerChunk)
        ChunkRange = int(self.ChunkRange)
        self.cy = []
        for cry in range(ChunkRange):
            for iy in range(BlockPerChunk):
                row = []  # Create a new empty list for each row
                for crx in range(ChunkRange):
                    for ix in range(BlockPerChunk):
                        row.append(random.randint(0, 1))
                self.cy.append(row)  # Append the complete row to cy
        with open(self.MapPath, 'w+') as file:
            for row in self.cy:  # Write each row without brackets
                file.write(''.join(map(str, row)) + '\n')  # Join row elements and add newline
    def printc(self):
        for row in self.cy:
            print(''.join(map(str, row)))  # Join elements and print without brackets

class loadmap():
    def __init__(self,MapName,Screen):
        self.MapName = MapName
        self.pathname ="Data\\Game\\Maps\\"+MapName+".txt"
        if not os.path.exists(self.pathname):
          print("Error")
          breakpoint
        self.start = 0
        self.starty = 0
        self.Screen = Screen
        self.Stx = 0
        self.Sty = 0
    def LoadTile(self):
        self.DisplayBlock = []
        self.ClickTile = False
        a = CreateButtonImages(ImportTile.dirt,0,0,self.Screen)
        x = CreateButtonImages(ImportTile.grass,0,0,self.Screen)
        self.tileListX = []
        self.tileListY = []
        countx = 0
        county = 0
        self.Chunky = []
        self.TouchPos = dict(tile="",BlockX=0,BlockY=0,PosX=0,PosY=0)
        self.TouchPos["tile"]="Air"
        with open(self.pathname, "r") as self.file:
            for row in self.file:
                self.Chunky.append(row)
                for ppo in row:
                    if ppo == "1":
                        tile = ImportTile.grass  
                    elif ppo == "2":
                        tile = ImportTile.sand
                    elif ppo == "3":
                        tile = ImportTile.water      
                    else:
                        tile = ImportTile.dirt
                    self.tileListX.insert(countx,dict(Name=tile.Name,TileName=tile,Surface=self.Screen,PosX=self.start*tile.ScaleX,PosY=self.starty*tile.ScaleY,BlockPosX=self.start,BlockPosY=self.starty))
                    countx += 1
                    self.start += 1
                self.tileListY.insert(county,self.tileListX)
                self.tileListX = []
                self.starty += 1
                self.start = 0
                county +=1
    def UpdateMoving(self):
        k = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_pos()
        if k[pygame.K_d] or mx > 980:
            if self.Stx < 90:
                self.Stx+=1
            else:
                pass
        if k[pygame.K_a] or mx < 20:
            if self.Stx > 0:
                self.Stx -=1
            else:
                pass
        if k[pygame.K_s] or screeny-my < 25:
            if self.Sty < 90:
                self.Sty+=1
            else:
                pass
        if k[pygame.K_w]or my < 20:
            if self.Sty > 0:
                self.Sty -=1
            else:
                pass
        pygame.time.delay(25)
        
        pass
    def DrawTile(self):
        for x in range(10):
            for b in range(10):
                g = self.tileListY[x+int(self.Sty)]
                a = g[b+int(self.Stx)]
                Nametile = a["TileName"]
                Nametile.Draw(a["Surface"],(b*a["TileName"].ScaleX),(x*a["TileName"].ScaleY))
                BoxCol = Rect((b*a["TileName"].ScaleX),(x*a["TileName"].ScaleY),a["TileName"].ScaleX,a["TileName"].ScaleY)
                
                if BoxCol.collidepoint(pygame.mouse.get_pos()):
                    au = slot((0,0,0),(0,0,0),a["TileName"].ScaleX-10,a["TileName"].ScaleY-10,3,(b*a["TileName"].ScaleX+5),(x*a["TileName"].ScaleY+5))
                    au.Draw(screen)
                    pass
                if BoxCol.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() and self.ClickTile == False:
                    self.TouchPos["tile"]=a["Name"]
                    self.TouchPos["BlockX"]= a["BlockPosX"]
                    self.TouchPos["BlockY"]= a["BlockPosY"]
                    self.TouchPos["PosX"]=b*50
                    self.TouchPos["PosY"]=x*50
                    self.ClickTile = True
                    print(self.TouchPos)
                    if pygame.mouse.get_pressed()[0]:
                        ct = ImportTile.water
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                    if pygame.mouse.get_pressed()[2]:
                        ct = ImportTile.sand
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                    if pygame.mouse.get_pressed()[1]:
                        ct = ImportTile.grass
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                if not pygame.mouse.get_pressed()[0]:
                    self.ClickTile = False
        pygame.display.flip()

    

