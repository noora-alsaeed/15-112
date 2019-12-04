import pygame
import sys

width  = 1000
height = 600

class Stage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.move1 = 0  # movement of background
        self.background = pygame.image.load("bg.png")
        
        self.NPCGroup = pygame.sprite.Group()
        
        self.NPC = Mystique()
        self.NPC.rect.x = 400
        self.NPC.rect.y = height - self.NPC.rect.height
        self.NPCGroup.add(self.NPC)
        
        self.NPC = Mubarak()
        self.NPC.rect.x = 1000
        self.NPC.rect.y = height - self.NPC.rect.height
        self.NPCGroup.add(self.NPC)
        
    def neededMovement(self, numberMove):
        self.move1 += numberMove
        for NPC in self.NPCGroup:
            NPC.rect.x += numberMove
        
    def update(self):
        self.NPCGroup.update()
        
    def draw(self, windowDisplay):
        windowDisplay.fill((255, 255, 255))
        windowDisplay.blit(self.background,(self.move1 , 0))
        self.NPCGroup.draw(windowDisplay)

class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("hammer.png")
        image = pygame.transform.scale(image, (92, 92))
        image = pygame.transform.rotate(image, 45)
        self.image = image
        self.rect = self.image.get_rect()
        
        self.heart = 6
        self.x = 0
        self.y = 0
        
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
                    
    
    def collide(self, other):
        return self.rect.colliderect(other.rect)
    
    def goLeft(self):
        self.x = -6

        
    def goRight(self):
        self.x = 6

    def fly(self):
        self.y = -6
    
    def descend(self):
        self.y = 6
    
    def stopHorizontal(self):
        self.x = 0
    
    def stopVertical(self):
        self.y = 0
    
class GameHammer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.vertical = "U" # Initial vertical direction
        self.horizontal = "R" # Initial horizontal direction
        self.click = False
        
        self.beginPoint1 = 500
        self.turnPoint1 = 300
        self.beginPoint2 = 250
        self.turnPoint2 = 310
        
        self.speed1 = 5 # Ascending and Descending Speed
        self.speed2 = 3 # Left and Right Speed
        
        image = pygame.image.load("hammer.png")
        image = pygame.transform.scale(image, (92, 92))
        image = pygame.transform.rotate(image, -45)
        self.image = image
        self.rect = self.image.get_rect()
        
    def update(self):
        if self.click == False:
            if not self.speed1 > 0: 
                self.vertical = "U" 
                if (self.turnPoint1 - self.speed1) < self.rect.y: 
                    self.rect.y += self.speed1
                else:
                    self.speed1 = (-1 * self.speed1)
                    self.rect.y += self.speed1
            else: 
                self.vertical = "D"
                if (self.beginPoint1 + self.speed1) > self.rect.y: 
                    self.rect.y += self.speed1
                else: 
                    self.speed1 = (-1 * self.speed1)
                    self.rect.y += self.speed1
        else:
            if not self.speed2 > 0: 
                self.horizontal = "R" 
                if (self.beginPoint2 - self.speed2) < self.rect.x: 
                    self.rect.x += self.speed2
                else:
                    self.speed2 = (-1 * self.speed2)
                    self.rect.x += self.speed2
                    self.click = False
            else: 
                self.horizontal = "L"
                if (self.turnPoint2 + self.speed2) > self.rect.x: 
                    self.rect.x += self.speed2
                else: 
                    self.speed2 = (-1 * self.speed2)
                    self.rect.x += self.speed2
                    
    
    def collide(self, other):
        return self.rect.colliderect(other.rect)
        
    def clicked(self):
        self.click = True
    
    def unclicked(self):
        self.click = False
                
                
class Mystique(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("mystique.png")
        image = pygame.transform.scale(image, (100, 100))
        self.image = image
        self.rect = self.image.get_rect()
        
class Mubarak(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("happyMub.png")
        image = pygame.transform.scale(image, (100, 100))
        self.image = image
        self.rect = self.image.get_rect()
class Heel1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("feet1.png")
        image = pygame.transform.scale(image, (1000, 1000))
        self.image = image
        self.rect = self.image.get_rect()
        self.collided = True
        
    def update(self):
        if self.collided == False:
            self.rect.y += 1
        else:
            self.rect.y = self.rect.y
    
    def collision(self, other):
        return self.rect.colliderect(other.rect)
        
    def flyDown(self):
        self.collided = False
    
    def stop(self):
        self.collided = True
    
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("tempHeel.png")
        image = pygame.transform.scale(image, (80, 80))
        self.image = image
        self.rect = self.image.get_rect()
        
        self.collided = False
        
    def update(self):
        if self.collided == True:
            self.rect.x += 30
        
            
    
    def flyAway(self):
        self.collided = True
    
class Heel2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("footMub.png")
        image = pygame.transform.scale(image, (500, 500))
        self.image = image
        self.rect = self.image.get_rect()

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("gun.png")
        image = pygame.transform.scale(image, (92, 92))
        self.image = image
        self.rect = self.image.get_rect()
        
        self.heart = 6
        self.x = 0
        self.y = 0
        
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
                    
    
    def collide(self, other):
        return self.rect.colliderect(other.rect)
    
    def goLeft(self):
        self.x = -6

        
    def goRight(self):
        self.x = 6

    def fly(self):
        self.y = -6
    
    def descend(self):
        self.y = 6
    
    def stopHorizontal(self):
        self.x = 0
    
    def stopVertical(self):
        self.y = 0
        
        
        
class GameGun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.vertical = "U" # Initial vertical direction
        self.horizontal = "R" # Initial horizontal direction
        self.click = False
        
        self.beginPoint1 = 500
        self.turnPoint1 = 300
        self.beginPoint2 = 250
        self.turnPoint2 = 310
        
        self.speed1 = 5 # Ascending and Descending Speed
        self.speed2 = 3 # Left and Right Speed
        
        image = pygame.image.load("gun.png")
        image = pygame.transform.scale(image, (92, 92))
        self.image = image
        self.rect = self.image.get_rect()
        
    def update(self):
        if self.click == False:
            if not self.speed1 > 0: 
                self.vertical = "U" 
                if (self.turnPoint1 - self.speed1) < self.rect.y: 
                    self.rect.y += self.speed1
                else:
                    self.speed1 = (-1 * self.speed1)
                    self.rect.y += self.speed1
            else: 
                self.vertical = "D"
                if (self.beginPoint1 + self.speed1) > self.rect.y: 
                    self.rect.y += self.speed1
                else: 
                    self.speed1 = (-1 * self.speed1)
                    self.rect.y += self.speed1

                    
    
    def collide(self, other):
        return self.rect.colliderect(other.rect)
        
           
           
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 5
        
    def collide(self, other):
        return self.rect.colliderect(other.rect)
        
