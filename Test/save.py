import pygame
import sys
from pygame import *
import random 
import os
import ImportTile
import math

import Data
screenx = Data.GameWidth
screeny = Data.GameHeight 
pygame.font.init()
font = pygame.font.Font(None, 36)

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
class CreateButtonImages(): #Image PosX PosY Surface
    def __init__(self, Images, PosX, PosY, Surface):
        self.Images = Images
        self.PosX = PosX
        self.PosY = PosY
        self.Surface = Surface
        self.ImageScaleX = self.Images.ScaleX
        self.ImageScaleY = self.Images.ScaleY
        self.Image = Rect(self.PosX, self.PosY, self.ImageScaleX, self.ImageScaleY)
        self.CheckClick = False
    def Draw(self, Execute):
        self.Execute = Execute
        self.Images.Draw(self.Surface,self.PosX,self.PosY)
        if self.Image.collidepoint(pygame.mouse.get_pos()) :
            if pygame.mouse.get_pressed()[0] and not self.CheckClick:
                self.CheckClick = True
                Execute()
            if not pygame.mouse.get_pressed()[0]:
                self.CheckClick = False

    def DrawScale(self, Execute,ScaleX,ScaleY):
        self.Images.DrawScale(self.Surface,self.PosX,self.PosY,ScaleX,ScaleY)
        if self.Image.collidepoint(pygame.mouse.get_pos()) :
            if pygame.mouse.get_pressed()[0] and not self.CheckClick:
                self.CheckClick = True
                Execute()
            if not pygame.mouse.get_pressed()[0]:
                self.CheckClick = False
def fcc(): #FullScreen Toggle

    if fc == True:

        ctypes.windll.user32.SetProcessDPIAware()

        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        pygame.display.set_mode(true_res,pygame.FULLSCREEN)

    else:

        screen = pygame.display.set_mode((1000,720))
class HoldDragMouse():
    def __init__(self,ColorLine,LineWidth,Surface):
        self.ColorLine = ColorLine
        self.LineWidth = LineWidth
        self.Surface = Surface
        self.DragMouse = False
        MouseEvenDrag = self.DragMouse
        self.RectDone= 0
        self.MouseStartX,self.MouseStartY = 0, 0
        self.MouseEndX, self.MouseEndY = 0, 0
        self.Sx = 0
        self.Sy = 0
        self.Ex = 0 
        self.Ey = 0
    def Run(self):
        
        if pygame.mouse.get_pressed()[0] and self.DragMouse == False:
            self.MouseStartX,self.MouseStartY = pygame.mouse.get_pos()
            self.DragMouse = True
            
        if not pygame.mouse.get_pressed()[0] or self.DragMouse == False:
            self.MouseStartX,self.MouseStartY = 0, 0
            self.MouseEndX, self.MouseEndY = 0, 0
            self.Sx = 0
            self.Sy = 0
            self.Ex = 0 
            self.Ey = 0
            self.DragMouse = False
            Data.MouseDragRect = Rect(0,0,0,0)
        if self.DragMouse == True:
            self.MouseEndX, self.MouseEndY = pygame.mouse.get_pos()
            if self.MouseEndX== self.MouseStartX or self.MouseStartY ==self.MouseEndY:
                Data.MouseDrag = False
                
            else : Data.MouseDrag = True
            if self.MouseStartX < self.MouseEndX:
                self.Sx = self.MouseStartX
                self.Ex = self.MouseEndX
            elif self.MouseStartX > self.MouseEndX:
                self.Ex = self.MouseStartX
                self.Sx = self.MouseEndX
            if self.MouseStartY < self.MouseEndY:
                self.Sy = self.MouseStartY
                self.Ey = self.MouseEndY
            elif self.MouseStartY > self.MouseEndY:
                self.Ey = self.MouseStartY
                self.Sy = self.MouseEndY
            self.FullCollBox = Rect(self.Sx,self.Sy,abs(self.Ex-self.Sx),abs(self.Ey-self.Sy))
            Data.MouseDragRect = Rect(self.Sx,self.Sy,abs(self.Ex-self.Sx),abs(self.Ey-self.Sy))
            pygame.draw.rect(self.Surface,(0,100,200),self.FullCollBox)
            pygame.draw.line(self.Surface,self.ColorLine,(self.MouseStartX,self.MouseStartY),(self.MouseEndX,self.MouseStartY),self.LineWidth)
            pygame.draw.line(self.Surface,self.ColorLine,(self.MouseStartX,self.MouseEndY),(self.MouseEndX,self.MouseEndY),self.LineWidth)
            pygame.draw.line(self.Surface,self.ColorLine,(self.MouseStartX,self.MouseStartY),(self.MouseStartX,self.MouseEndY),self.LineWidth)
            pygame.draw.line(self.Surface,self.ColorLine,(self.MouseEndX,self.MouseStartY),(self.MouseEndX,self.MouseEndY),self.LineWidth)

    pass
class Player():
    def __init__(self, health, speed, pos):
        self.health = health
        self.speed = speed
        self.pos = Vector2(pos)
        self.velocity = Vector2(0, 0)

    def spawn(self, screen):
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 50, 50)
        pygame.draw.rect(screen, "green", self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        self.velocity = Vector2(0, 0)

        if keys[pygame.K_w]:
            self.velocity.y = -self.speed
        if keys[pygame.K_s]:
            self.velocity.y = self.speed
        if keys[pygame.K_a]:
            self.velocity.x = -self.speed
        if keys[pygame.K_d]:
            self.velocity.x = self.speed

        self.pos += self.velocity

        # Ensure player stays within screen bounds
        self.pos.x = max(0, min(screenx - 50, self.pos.x))
        self.pos.y = max(0, min(screeny - 50, self.pos.y))

        pygame.time.delay(25)
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
        self.DisplayTileY = []
        countx = 0
        county = 0
        self.Chunky = []
        self.TouchPos = dict(tile="",BlockX=0,BlockY=0,PosX=0,PosY=0,CenterX=0,CenterY=0,MapPosX=0,MapPosY=0,DsX=0,DsY=0)
        self.TouchPos["tile"]="Air"
        xa = 0
        ya= 0
        with open(self.pathname, "r") as self.file:
            for row in self.file:
                self.Chunky.append(row)
                if ya >= 9:
                    ya= 0
                for ppo in row:
                    if xa >= 9:
                        xa=0
                    if ppo == "1":
                        tile = ImportTile.grass  
                    elif ppo == "2":
                        tile = ImportTile.sand
                    elif ppo == "3":
                        tile = ImportTile.water      
                    else:
                        tile = ImportTile.dirt
                    self.tileListX.insert(countx,dict(Name=tile.Name,TileName=tile,Surface=self.Screen,PosX=self.start*tile.ScaleX,PosY=self.starty*tile.ScaleY,BlockPosX=self.start,BlockPosY=self.starty,CenterX=self.start*tile.ScaleX+(tile.ScaleX/2),CenterY=self.start*tile.ScaleY+(tile.ScaleY/2)))
                    countx += 1
                    self.start += 1
                    xa +=1
                ya+=1
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
    def ObjectProp(self,MaxProp):
        self.MaxProp= MaxProp
        self.CurrentProp = 0
        mx, my = pygame.mouse.get_pos()
        self.PropList = []


    def ImportDisplayTile(self):
        for x in range(10): #LoadDisPlay Tile And Draw Tile
            DisplayTileX = []
            for b in range(10):
                g = self.tileListY[x+int(self.Sty)]
                a = g[b+int(self.Stx)]
                DisplayTileX.append(dict(PosX=b*a["TileName"].ScaleX,PosY=x*a["TileName"].ScaleY,BlockX=a["BlockPosX"],BlockY=a["BlockPosY"]))
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
                    self.TouchPos["CenterX"]= a["CenterX"]
                    self.TouchPos["CenterY"]= a["CenterY"]
                    self.TouchPos["PosX"]=b*50
                    self.TouchPos["PosY"]=x*50
                    self.TouchPos["MapPosX"]=a["PosX"]
                    self.TouchPos["MapPosY"]=a["PosY"]
                    self.ClickTile = True
                    if pygame.mouse.get_pressed()[0]:
                        ct = ImportTile.water
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                        print(self.TouchPos)
                    if pygame.mouse.get_pressed()[2]:
                        ct = ImportTile.sand
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                        print(self.TouchPos)
                    if pygame.mouse.get_pressed()[1]:
                        ct = ImportTile.grass
                        a["TileName"]= ct
                        a["Name"]=ct.Name
                        print(self.TouchPos)
                        
                if not pygame.mouse.get_pressed()[0]:
                    self.ClickTile = False
            self.DisplayTileY.append(DisplayTileX)
            DisplayTileX = []
    def UpdateMiniMap(self):
        d=0
        for row in self.Chunky:
            a=0
            for letter in row:
                if letter == "1":
                    tile = ImportTile.grassmini  
                elif letter == "2":
                    tile = ImportTile.sandmini
                elif letter == "3":
                    tile = ImportTile.watermini      
                else:
                    tile = ImportTile.dirtmini
                tile.DrawScale(screen,a+700,d,2,2)
                a+=1
            d+=1
        
        pygame.display.flip()



class ListObjectGame():
    def __init__(self,LimitProp,Screen,PropList):
        self.LimitProp = LimitProp
       
        self.DragMouse = False
        self.PropList = []
        self.ClickOb = False
        self.ClickMove = False
        self.screen = Screen
        self.ChosePropONL = []
        self.LastMove = 0
        self.ChosePropMTO = []
        self.speed = {"Villager":150,"Guard":200,"HouresGuard":250}
        self.selected_prop_id = None
        self.grid_size = 25
        self.TargetPos = {}
        self.screen = screen
        self.GridX = []
        self.GridY = []
        self.CantNext = []
        self.dt = 1
    def get_grid_position(self):
        x, y = pygame.mouse.get_pos()
        return x // self.grid_size, y // self.grid_size

    def move(self, prop, delta_time, direction):
        move_distance = (self.speed.get(prop['Role'], 150) / 50) * delta_time
        target_x, target_y = prop["PosX"], prop["PosY"]
        
        if direction == 'X':
            target_x += self.dt
            prop["PosX"] = min(prop["PosX"] + move_distance, target_x)
        elif direction == '-X':
            target_x -= self.dt
            prop["PosX"] = max(prop["PosX"] - move_distance, target_x)
        elif direction == 'Y':
            target_y += self.dt
            prop["PosY"] = min(prop["PosY"] + move_distance, target_y)
        elif direction == '-Y':
            target_y -= self.dt
            prop["PosY"] = max(prop["PosY"] - move_distance, target_y)
        
        return target_x, target_y

    def is_obstacle_in_path(self, prop, target_x, target_y):
        for other_prop in self.PropList:
            if other_prop["ID"] != prop["ID"] and other_prop["PosX"] == target_x and other_prop["PosY"] == target_y:
                return True
        return False

    def Move(self, delta_time):
        mouse_pos = pygame.mouse.get_pos()
        selected_props = set(self.ChosePropONL + self.ChosePropMTO)
        if not pygame.mouse.get_pressed()[2]:
            self.ClickMove = False
        if pygame.mouse.get_pressed()[2] and self.ClickMove == False:
            self.ClickMove = True
            mouse_grid = self.get_grid_position()
            
            # Avoid duplicates by checking if the position is already in TargetPos
            existing_positions = set(self.TargetPos.values())
            if mouse_grid >(38,27):
                    mouse_grid = 38,mouse_grid[1]
            else:
                pass
            # If the position is already taken, find an adjacent position
            if mouse_grid in existing_positions:
                # Check all 4 adjacent cells
                potential_positions = [
                    (mouse_grid[0] - 1, mouse_grid[1]),  # Left
                    (mouse_grid[0] + 1, mouse_grid[1])  # Right
                     # Up
                   # Down
                ]
                
                # Find a position that is not already taken
                for pos in potential_positions:
                    if pos not in existing_positions:
                        mouse_grid = pos
                        break
               
                

            
            # Assign target positions
            for prop_id in selected_props:
                self.TargetPos[prop_id] = mouse_grid
        
        for prop in self.PropList:
            prop_id = prop['ID']
            if prop["IsPeople"] and prop_id in self.TargetPos:
                target_pos = self.TargetPos[prop_id]
                distance_x = abs(target_pos[0] - prop["PosX"])
                distance_y = abs(target_pos[1] - prop["PosY"])
                
                if distance_x >= distance_y:
                    if distance_x > 0.1:
                        if prop["PosX"] > target_pos[0]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"] - 1, prop["PosY"]):
                                self.move(prop, delta_time, '-X')
                            else:
                                self.move(prop, delta_time, '-Y' if prop["PosY"] >= (screeny // self.grid_size) else 'Y')
                        elif prop["PosX"] < target_pos[0]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"] + 1, prop["PosY"]):
                                self.move(prop, delta_time, 'X')
                            else:
                                self.move(prop, delta_time, '-Y' if prop["PosY"] >= (screeny // self.grid_size) else 'Y')
                    elif distance_y > 0.1:
                        if prop["PosY"] > target_pos[1]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"], prop["PosY"] - 1):
                                self.move(prop, delta_time, '-Y')
                            else:
                                self.move(prop, delta_time, '-X' if prop["PosY"] >= (screenx - 200 // self.grid_size) else '-X')
                        elif prop["PosY"] < target_pos[1]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"], prop["PosY"] + 1):
                                self.move(prop, delta_time, 'Y')
                            else:
                                self.move(prop, delta_time, '-X' if prop["PosY"] >= (screenx - 200 // self.grid_size) else '-X')
                else:
                    if distance_y > 0.1:
                        if prop["PosY"] > target_pos[1]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"], prop["PosY"] - 1):
                                self.move(prop, delta_time, '-Y')
                            else:
                                self.move(prop, delta_time, '-X' if prop["PosY"] >= (screenx - 200 // self.grid_size) else '-X')
                        elif prop["PosY"] < target_pos[1]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"], prop["PosY"] + 1):
                                self.move(prop, delta_time, 'Y')
                            else:
                                self.move(prop, delta_time, '-X' if prop["PosY"] >= (screenx - 200 // self.grid_size) else '-X')
                    elif distance_x > 0.1:
                        if prop["PosX"] > target_pos[0]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"] - 1, prop["PosY"]):
                                self.move(prop, delta_time, '-X')
                            else:
                                self.move(prop, delta_time, '-Y' if prop["PosY"] >= (screeny // self.grid_size) else 'Y')
                        elif prop["PosX"] < target_pos[0]:
                            if not self.is_obstacle_in_path(prop, prop["PosX"] + 1, prop["PosY"]):
                                self.move(prop, delta_time, 'X')
                            else:
                                self.move(prop, delta_time, '-Y' if prop["PosY"] >= (screeny // self.grid_size) else 'Y')
                pygame.draw.line(self.screen,(100,0,150),((prop['PosX']*25)+25,(prop['PosY']*25)+25),((target_pos[0]*25)+25,(target_pos[1]*25)+25))
                if round(distance_x) < 0.1 and round(distance_y) < 0.1:
                    del self.TargetPos[prop_id]
                    prop["PosX"], prop["PosY"] = round(prop["PosX"]), round(prop["PosY"])

                self.CantNext[self.PropList.index(prop)].update({"X": prop["PosX"], "Y": prop["PosY"]})

    def draw_grid(self):
        self.GridX, self.GridY = [], []
        for y in range(0, screeny, self.grid_size):
            for x in range(0, screenx-200, self.grid_size):
                rect = pygame.Rect(x, y, self.grid_size, self.grid_size)
                pygame.draw.rect(screen, (50, 0, 100), rect, 1)  # Draw grid lines

                grid_x, grid_y = x // self.grid_size, y // self.grid_size
                mouse_pos = pygame.mouse.get_pos()
                grid_x = mouse_pos[0] // self.grid_size
                grid_y = mouse_pos[1] // self.grid_size
                self.GridX.append(dict(XPos=grid_x, YPos=grid_y, X=x, Y=y))
                
                coord_text = f"{grid_x},{grid_y}"
                text = font.render(coord_text, True, (0, 0, 0))  # Black color for text
                screen.blit(text, (10, 10))
            self.GridY.append(self.GridX.copy())
            self.GridX.clear()
    def execute(self):
        if self.ChosePropMTO == []:
            self.PropExecute = self.ChosePropONL
        else:
            self.PropExecute = self.ChosePropMTO
        if len(self.PropExecute) > 1:
            self.MorePropExecute(self.PropExecute)
        else:
            self.OnePropExecute(self.PropExecute).MoveOneProp()
    
      

    pygame.display.flip()  # Cập nhật màn hình   
    def CreateProp(self,ID,PosX,PosY,Scale,Role,IsPeople,Texture=0):
        self.PosX = PosX
        self.PosY = PosY
        self.Scale = Scale
        self.Texture = Texture
        self.Role = Role
        self.IsPeople = IsPeople
        self.ID = ID
        
        if self.LimitProp > len(self.PropList):
            
            self.PropList.append(dict(
                ID=self.ID,
                PosX=self.PosX//self.grid_size,
                PosY=self.PosY//self.grid_size,
                CenterX=self.PosX+(self.Scale//2),
                CenterY=self.PosY+(self.Scale//2),
                Scale=self.Scale,
                Texture=self.Texture,
                Role=self.Role,
                IsPeople=self.IsPeople,
                IsChose=False
                ))  
            self.CantNext.append(dict(X=self.PosX//self.grid_size,Y=self.PosY//self.grid_size))         
            return True 
        else : return False
    def LoadProp(self):
        if not Data.MouseDragRect.colliderect == None and pygame.mouse.get_pressed()[0] :
                self.ChosePropMTO = []
        if len(self.ChosePropMTO) > 0:
             self.ChosePropONL = []
        if not pygame.mouse.get_pressed()[0]:
            self.ClickOb = False
        if pygame.mouse.get_pressed()[0] and self.ClickOb == False:
            self.ChosePropONL = []
            self.ClickOb == True
        for PropCount in self.PropList:
            self.HitBox = Rect(PropCount["PosX"]*self.grid_size,PropCount["PosY"]*self.grid_size,PropCount["Scale"],PropCount["Scale"])
            if PropCount["Texture"] == 0:
                PropFace = Rect(PropCount["PosX"]*self.grid_size,PropCount["PosY"]*self.grid_size,PropCount["Scale"],PropCount["Scale"])
                pygame.draw.rect(screen,(255,255,255),PropFace)
            else:
                PropFace = PropCount["Texture"]    
                PropFace.DrawScale(screen,PropCount["PosX"]*self.grid_size,PropCount["PosY"]*self.grid_size,PropCount["Scale"],PropCount["Scale"])
            for checkchose in self.ChosePropONL:
                if PropCount["ID"]== checkchose:
                    Sc = slot((50,255,50),(0,0,0),PropCount["Scale"]-3,PropCount["Scale"]-3,3,(PropCount["PosX"]*self.grid_size)+1.5,(PropCount["PosY"]*self.grid_size+1.5))
                    Sc.Draw(self.screen)
            for checkchoseA in self.ChosePropMTO:
                if PropCount["ID"]== checkchoseA:
                    Sc = slot((100,255,50),(0,0,0),PropCount["Scale"]-3,PropCount["Scale"]-3,3,(PropCount["PosX"]*self.grid_size)+1.5,(PropCount["PosY"]*self.grid_size)+1.5)
                    Sc.Draw(self.screen)
            if self.HitBox.collidepoint(pygame.mouse.get_pos()) :
                if PropCount["ID"] not in self.ChosePropMTO or PropCount["ID"] not in self.ChosePropONL:
                    Sel = slot((0,0,0),(0,0,0),PropCount["Scale"]-10,PropCount["Scale"]-10,3,(PropCount["PosX"]*self.grid_size)+5,(PropCount["PosY"]*self.grid_size)+5)
                    Sel.Draw(self.screen)
                if pygame.mouse.get_pressed()[0] and self.ClickOb == False:
                    if PropCount["Role"] == 'Villager':
                        Data.Sc1ForViler = True
                    else:
                        Data.Sc1ForViler = False
                    self.ClickOb == True
                    if self.HitBox.collidepoint(pygame.mouse.get_pos())and Data.MouseDrag == False:
                        self.ChosePropMTO = []
                        self.ChosePropONL = []
                        if PropCount["IsPeople"] == True:
                            self.ChosePropONL.append(PropCount["ID"])
            if self.HitBox.colliderect(Data.MouseDragRect):
                self.ChosePropONL = []
                if PropCount["IsPeople"] == True:
                    self.ChosePropMTO.append(PropCount["ID"])


          
            
p = ListObjectGame(100,screen,"A")

p.CreateProp("Man",500,350,50,"Villager",True,ImportTile.Player)
p.CreateProp("Man2",500,100,50,"Guard",True,ImportTile.Player)


