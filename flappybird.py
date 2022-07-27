from turtle import distance
import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 350
WINDOWHEIGHT = 600
BACKGROUND = pygame.image.load('img/background.png')

BIRDWIDTH = 20
BIRDHEIGHT = 20
G = 0.1
SPEEDFLY = -8
BIRDIMG = pygame.image.load('img/bird.png')

COLUMNWIDTH = 60
COLUMNHEIGHT = 300
BLANK = 60 
DISTANCE = 200
COLUMNSPEED = 1
COLUMNIMG = pygame.image.load('img/column.png')


class Bird():
    def __init__(self):
        
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/4
        self.y = (WINDOWHEIGHT- self.height)/2
        self.speed = 0
        self.suface = BIRDIMG
    def draw(self):
        #bird = pygame.display.set_mode((60,60))
        DISPLAYSURF.blit(self.suface, (int(self.x), int(self.y)))

    def update(self, mouseClick):
        self.y += self.speed + 0.5*G
        self.speed += G

        if mouseClick == True:
            self.speed = SPEEDFLY

class Column():
    def __init__(self):
        self.width = COLUMNWIDTH
        self.height = COLUMNHEIGHT
        self.blank = BLANK
        self.distance = DISTANCE
        self.speed = COLUMNSPEED
        self.surface = COLUMNIMG
        self.ls = []
        for i in range(3):
            x = WINDOWWIDTH + i*self.distance
            # x = i*self.distance
            #y = random.randrange(60, WINDOWHEIGHT - 60 - self.blank, 20 )
            y = 80
            self.ls.append([x,y])
        
    def draw(self):
        for i in range(3): 
            DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1]) - self.height))
            DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1]) + self.height))

    def update(self):
        for i in range(3): 
            self.ls[i][0] -= self.speed
        #if self.ls[0][0] < 0
        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = 80
            self.ls.append([x,y])

        
           

            

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Game cui bap')

def main():
    
    bird = Bird()
    column = Column()
    while True:
        mouseClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouseClick = True
        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        bird.draw()
        column.draw()
        bird.update(mouseClick)
        column.update()

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()