import pygame
import sys

import heel

pygame.init()

####################
# Name: Noora Al-Saeed
# Term Project: Break the Heel
# Description: (https://www.youtube.com/watch?v=7KSV-0qk3yU) My term project is game based on the game "Kakato Oteshi". It's main purpose 
# is knocking down a person's shoe heels with a hammer until all the heel blocks are gone.

# Series Tutorials I've Watched:
# https://www.youtube.com/watch?v=i6xMBig-pP4
# https://www.youtube.com/watch?v=uWvb3QzA48c
# https://www.youtube.com/watch?v=ujOTNg17LjI

####################



####################
#
# Colors
#
####################

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 156, 255)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255,140,0)

########## Dimensions

width  = 1000
height = 600


########## Initalizations
windowDimensions = [width, height]
windowDisplay = pygame.display.set_mode(windowDimensions)


spritesGroup = pygame.sprite.Group()
heelGroup = pygame.sprite.Group()
blockGroup = pygame.sprite.Group()

music = pygame.mixer.music.load("main.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()


########## Main Loops

####################
#
# Main Screen
#
####################

mainScreen = False

while mainScreen == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mainScreen = True


    intro = pygame.image.load("/pictures/heel.jpg").convert()
    intro = pygame.transform.scale(intro, (40, 40))
    windowDisplay.fill(white)
    windowDisplay.blit(intro, (width//2.1,height//2.4))
    
    font1 = pygame.font.SysFont('Comic Sans MS', 90)
    font2 = pygame.font.SysFont('Comic Sans MS', 40)
    
    title = font1.render('Break the Heel' , 1, black)
    caption = font2.render('Press "P" to play!' , 1, black)
    

    windowDisplay.blit(title, (width//2 - 230, height//2 - 150))
    windowDisplay.blit(caption, (width//2.7, height//2 + 50 ))


    pygame.display.update()
    clock.tick(15)


####################
#
# Prologue
#
####################

prologue = False
angry = False

while prologue == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                prologue = True
            elif event.key == pygame.K_n:
                angry = True
    if angry == False:
        intro = pygame.image.load("/pictures/face.png").convert()
        intro = pygame.transform.scale(intro, (width//2, height))
        windowDisplay.fill(black)
        windowDisplay.blit(intro, (width//4.5,0))
            
        font1 = pygame.font.SysFont('Comic Sans MS', 40)
            
        caption1 = font1.render('My heels are too much, ugh! Can you fix them for me?' , 1, white)
        caption2 = font1.render('Press "Y" to accept / Press "N" to decline' , 1, white)
        windowDisplay.blit(caption2, (width//2 - 280, height//2 - 270))
        windowDisplay.blit(caption1, (width//2 - 350, height//2 + 230))

        
    else:
        intro = pygame.image.load("/pictures/angry.png").convert()
        intro = pygame.transform.scale(intro, (width//2, height))
        windowDisplay.fill(black)
        windowDisplay.blit(intro, (width//4.5,0))
        
        font1 = pygame.font.SysFont('Comic Sans MS', 40)

            
        caption1 = font1.render('Excuse me? Fix them NOW!' , 1, white)
        caption2 = font1.render('Press "Y" to accept' , 1, white)
        
        windowDisplay.blit(caption1, (width//2 - 220, height//2 + 230))
        windowDisplay.blit(caption2, (width//2 - 150, height//2 - 290))


    pygame.display.update()
    clock.tick(15)
    
####################
#
# First Level
#
####################

# Hammer
hammer = heel.Hammer()
hammer.rect.x = 250  # x pos of hammer
hammer.rect.y = 10 # y pos of hammer
spritesGroup.add(hammer)

# Foot
heel1 = heel.Heel1()
heel1.rect.x = 30  
heel1.rect.y = height - heel1.rect.height - 50
heelGroup.add(heel1)

# Heel Blocks 
block = heel.Block()
block.rect.x = 440  
block.rect.y = 480
blockGroup.add(block)

block = heel.Block()
block.rect.x = 440  
block.rect.y = 530
blockGroup.add(block)

block = heel.Block()
block.rect.x = 440  
block.rect.y = 430
blockGroup.add(block)



level = False
while level == False: # Main Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            level = True 
            pygame.quit()
            sys.exit(0)
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hammer.clicked()
    
    windowDisplay.fill(white)
    
    for i in blockGroup:
        for c in spritesGroup:
            if c.collision(i):
                i.flyAway()
                
                
    spritesGroup.draw(windowDisplay)
    blockGroup.draw(windowDisplay)
    heelGroup.draw(windowDisplay)
    spritesGroup.update()
    blockGroup.update()
    heelGroup.update()
    pygame.display.update()

    
    
pygame.quit()
