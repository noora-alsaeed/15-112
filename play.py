import pygame
import sys

import stage

pygame.init()

####################
# Name: Noora Al-Saeed
# Term Project: Break the Heel
# Description: (https://www.youtube.com/watch?v=7KSV-0qk3yU) My term project is a game based on the game "Kakato Oteshi". It's main purpose 
# is knocking down a person's shoe heels with a hammer until all the heel blocks are gone.

# Series Tutorials I've Watched:
# https://www.youtube.com/watch?v=i6xMBig-pP4
# https://www.youtube.com/watch?v=uWvb3QzA48c
# https://www.youtube.com/watch?v=ujOTNg17LjI
# https://www.youtube.com/watch?v=QplXBw_NK5Y

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
blockGroup = pygame.sprite.Group()
heelGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

blockGroup2 = pygame.sprite.Group()
heelGroup2 = pygame.sprite.Group()

gameHammerGroup = pygame.sprite.Group()

music = pygame.mixer.music.load("main.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()


########## Main Loops

mainScreen = False

while mainScreen == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mainScreen = True


    intro = pygame.image.load("heel.jpg").convert()
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



difficulty = False
weapon = ""
whichOne = ""

while difficulty == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                difficulty = True
                weapon = stage.Gun()
                whichOne = "p"
            elif event.key == pygame.K_h:
                difficulty = True
                weapon = stage.Hammer()
                whichOne = "h"


    intro = pygame.image.load("gun.png")
    intro = pygame.transform.scale(intro, (100, 100))
    windowDisplay.fill(white)
    windowDisplay.blit(intro, (width//4 ,height//2.4))
    
    intro = pygame.image.load("hammer.png")
    intro = pygame.transform.scale(intro, (100, 100))
    windowDisplay.blit(intro, (width//1.4,height//2.4))
    
    font1 = pygame.font.SysFont('Comic Sans MS', 90)
    font2 = pygame.font.SysFont('Comic Sans MS', 40)
    
    title = font1.render('Choose your weapon' , 1, black)
    caption = font2.render('Press "P" for Pistol or "H" for Hammer!' , 1, black)
    

    windowDisplay.blit(title, (width//2 - 230, height//2 - 150))
    windowDisplay.blit(caption, (width//2.7, height//2 + 50 ))


    pygame.display.update()
    clock.tick(15)





hammer = weapon
hammer.rect.x = 200  # starting x position of character
hammer.rect.y = height - hammer.rect.height  
spritesGroup.add(hammer)

if whichOne == "h":
    gameHammer = stage.GameHammer()
    gameHammer.rect.x = 250  # x pos of hammer
    gameHammer.rect.y = 10 # y pos of hammer
    gameHammerGroup.add(gameHammer)

elif whichOne == "p":
    gameHammer = stage.GameGun()
    gameHammer.rect.x = 250  # x pos of hammer
    gameHammer.rect.y = 10 # y pos of hammer
    gameHammerGroup.add(gameHammer)
heel1 = stage.Heel1()
heel1.rect.x = 30  
heel1.rect.y = height - heel1.rect.height - 200
heelGroup.add(heel1)

heel2 = stage.Heel2()
heel2.rect.x = 200  
heel2.rect.y = height - heel2.rect.height - 320
heelGroup2.add(heel2)
# Heel Blocks 
block = stage.Block()
block.rect.x = 428 
block.rect.y = 280
blockGroup.add(block)

block = stage.Block()
block.rect.x = 428
block.rect.y = 440
blockGroup.add(block)

block = stage.Block()
block.rect.x = 428  
block.rect.y = 360
blockGroup.add(block)

block = stage.Block()
block.rect.x = 428  
block.rect.y = 520
blockGroup.add(block)

# Heel Blocks 
block = stage.Block()
block.rect.x = 428 
block.rect.y = 280
blockGroup2.add(block)

block = stage.Block()
block.rect.x = 428
block.rect.y = 440
blockGroup2.add(block)

block = stage.Block()
block.rect.x = 428  
block.rect.y = 360
blockGroup2.add(block)

block = stage.Block()
block.rect.x = 428  
block.rect.y = 520
blockGroup2.add(block)

NPCList = []

count = 0
gameStage = stage.Stage()
gameLoop = False

prologue = True
prologue2 = True
angry = False
angry2 = False
startMini = False
level = True

while gameLoop == False: # Main Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameLoop = True 
            pygame.quit()
            sys.exit(0)
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hammer.goLeft()
            elif event.key == pygame.K_RIGHT:
                hammer.goRight()
            elif event.key == pygame.K_UP:
                hammer.fly()
            elif event.key == pygame.K_DOWN:
                hammer.descend()
                

        

                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and hammer.x < 0:
                hammer.stopHorizontal()
            elif event.key == pygame.K_RIGHT and hammer.x > 0:
                hammer.stopHorizontal()
            elif event.key == pygame.K_UP and hammer.y < 0:
                hammer.stopVertical()
            elif event.key == pygame.K_DOWN and hammer.y > 0:
                hammer.stopVertical()
    
    if hammer.rect.right >= 490:
        scrollingAmount = hammer.rect.right - 490
        hammer.rect.right = 490
        gameStage.neededMovement(-scrollingAmount)
    elif hammer.rect.left <= 110:
        scrollingAmount = 110 - hammer.rect.left
        hammer.rect.left = 110
        gameStage.neededMovement(scrollingAmount)

    for NPC in gameStage.NPCGroup:
        while NPC not in NPCList:
            NPCList.append(NPC)
        if hammer.collide(NPCList[0]):
            prologue = False
            
    for NPC in gameStage.NPCGroup:
        if NPC not in NPCList:
            NPCList.append(NPC)
            
    if hammer.collide(NPCList[1]):
        prologue2 = False
    

    while prologue == False and count == 0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    prologue = True
                    startMini = True
                    level = False
                    count = 1
                elif event.key == pygame.K_n:
                    angry = True
        if angry == False:
            intro = pygame.image.load("face.png").convert()
            intro = pygame.transform.scale(intro, (width//2, height))
            windowDisplay.fill(black)
            windowDisplay.blit(intro, (width//4.5,0))
                
            font1 = pygame.font.SysFont('Comic Sans MS', 40)
                
            caption1 = font1.render('My heels are too much, ugh! Can you fix them for me?' , 1, white)
            caption2 = font1.render('Press "Y" to accept / Press "N" to decline' , 1, white)
            windowDisplay.blit(caption2, (width//2 - 280, height//2 - 270))
            windowDisplay.blit(caption1, (width//2 - 350, height//2 + 230))
    
            
        else:
            intro = pygame.image.load("angry.png").convert()
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
    

    while count == 1: # Main Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                level = True 
                pygame.quit()
                sys.exit(0)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if whichOne == "h":
                        gameHammer.clicked()
                    else:
                        if len(bulletGroup) < 2:
                            bullet = stage.Bullet()
                
                            bullet.rect.x = gameHammer.rect.x + 99
                            bullet.rect.y = gameHammer.rect.y
                            
                            bulletGroup.add(bullet)
                
        
        windowDisplay.fill(white)
        
        for i in blockGroup:
            for c in gameHammerGroup:
                if c.collide(i):
                    i.flyAway()
                    
        for i in blockGroup:
            if i.rect.x > width * 2:
                blockGroup.remove(i)
        
        for i in bulletGroup:
            if i.rect.x > width:
                bulletGroup.remove(i)
                
        for b in bulletGroup:
            for i in blockGroup:
                if b.collide(i):
                 blockGroup.remove(i)
                 bulletGroup.remove(b)
                 
        if len(blockGroup) < 1:
            count += 1
        
        windowDisplay.fill(white)
        gameHammerGroup.draw(windowDisplay)
        blockGroup.draw(windowDisplay)
        heelGroup.draw(windowDisplay)
        bulletGroup.draw(windowDisplay)
        bulletGroup.update()
        gameHammerGroup.update()
        blockGroup.update()
        heelGroup.update()
        pygame.display.update()
        
    
    while prologue2 == False and count == 2:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    prologue2 = True

                    count += 1
                elif event.key == pygame.K_n:
                    angry2 = True
        if angry2 == False:
            intro = pygame.image.load("happyMub.png").convert()
            intro = pygame.transform.scale(intro, (width//2, height))
            windowDisplay.fill(black)
            windowDisplay.blit(intro, (width//4.5,0))
                
            font1 = pygame.font.SysFont('Comic Sans MS', 40)
                
            caption1 = font1.render('Noora! Can you help me remove these blocks off my shoe?' , 1, white)
            caption2 = font1.render('Press "Y" to accept / Press "N" to decline' , 1, white)
            windowDisplay.blit(caption2, (width//2 - 280, height//2 - 270))
            windowDisplay.blit(caption1, (width//2 - 350, height//2 + 230))
    
            
        else:
            intro = pygame.image.load("disgustedMub.png").convert()
            intro = pygame.transform.scale(intro, (width//2, height))
            windowDisplay.fill(black)
            windowDisplay.blit(intro, (width//4.5,0))
            
            font1 = pygame.font.SysFont('Comic Sans MS', 40)
    
                
            caption1 = font1.render("Don't be rude Noora. Just get these blocks off my shoe" , 1, white)
            caption2 = font1.render('Press "Y" to accept' , 1, white)
            
            windowDisplay.blit(caption1, (width//2 - 220, height//2 + 230))
            windowDisplay.blit(caption2, (width//2 - 150, height//2 - 290))
    
    
        pygame.display.update()
        clock.tick(15)
    
    while count == 3: # Main Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                level = True 
                pygame.quit()
                sys.exit(0)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if whichOne == "h":
                        gameHammer.clicked()
                    else:
                        if len(bulletGroup) < 2:
                            bullet = stage.Bullet()
                            
                            bullet.rect.x = gameHammer.rect.x + 99
                            bullet.rect.y = gameHammer.rect.y
                            
                            bulletGroup.add(bullet)
                
        
        windowDisplay.fill(white)
        
        for i in blockGroup2:
            for c in gameHammerGroup:
                if c.collide(i):
                    i.flyAway()
                    
        for i in blockGroup2:
            if i.rect.x > width * 2:
                blockGroup2.remove(i)
            
        for i in bulletGroup:
            if i.rect.x > width:
                bulletGroup.remove(i)
                
        for b in bulletGroup:
            for i in blockGroup2:
                if b.collide(i):
                 blockGroup2.remove(i)
                 bulletGroup.remove(b)
                 
        if len(blockGroup2) < 1:
            count += 1

        windowDisplay.fill(white)
        gameHammerGroup.draw(windowDisplay)
        blockGroup2.draw(windowDisplay)
        heelGroup2.draw(windowDisplay)
        bulletGroup.draw(windowDisplay)
        bulletGroup.update()
        gameHammerGroup.update()
        blockGroup2.update()
        heelGroup2.update()
        pygame.display.update()
        
    
    
    
    gameStage.draw(windowDisplay)
    spritesGroup.draw(windowDisplay)
    
    spritesGroup.update()
    pygame.display.update()
    
pygame.quit()