import pygame


####################
# Dimensions
####################
width  = 1000
height = 600

gameDimensions = [width, height]
gameDisplay = pygame.display.set_mode(gameDimensions)

red = (255, 0, 0)

####################
#
# Classes
#
####################

class Hammer(pygame.sprite.Sprite):
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
        image = pygame.transform.scale(image, (100, 100))
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
                    
    
    def collision(self, other):
        return self.rect.colliderect(other.rect)
        
    def clicked(self):
        self.click = True
    
    def unclicked(self):
        self.click = False
                
class Heel1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("feet1.png")
        image = pygame.transform.scale(image, (1000, 1000))
        self.image = image
        self.rect = self.image.get_rect()
        
        
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.image.load("tempHeel.png")
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.rect = self.image.get_rect()
        
        self.collided = False
        
    def update(self):
        if self.collided == True:
            self.rect.x += 30
            
    
    def flyAway(self):
        self.collided = True
        
