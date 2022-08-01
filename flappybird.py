from turtle import distance
import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 350
WINDOWHEIGHT = 600
BACKGROUND = pygame.image.load('img/background.png')

BIRDWIDTH = 20
BIRDHEIGHT = 20
G = 0.1
SPEEDFLY = -2
BIRDIMG = pygame.image.load('img/bird.png')

COLUMNWIDTH = 60
COLUMNHEIGHT = 500
BLANK = 80 
DISTANCE = 200
COLUMNSPEED = 1
COLUMNIMG = pygame.image.load('img/column.png')

def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False

def isGameOver(bird, columns):
    for i in range(3):
        rectBird = [bird.x, bird.y, bird.width, bird.height]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if rectCollision(rectBird, rectColumn1) == True or rectCollision(rectBird, rectColumn2) == True:
            return True
    if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT:
        return True
    return False


class Bird():
    def __init__(self):
        
        self.width = BIRDWIDTH
        self.height = BIRDHEIGHT
        self.x = (WINDOWWIDTH - self.width)/4
        self.y = (WINDOWHEIGHT- self.height)/2
        self.speed = 1
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
            y = random.randrange(60, WINDOWHEIGHT - 60 - self.blank, 20 )
            #y = 100
            self.ls.append([x,y])
        
    def draw(self):
        for i in range(3): 
            #DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1]) - self.height))
            #DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1]) + self.height))
            DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1] - self.height )))
            DISPLAYSURF.blit(self.surface, (int(self.ls[i][0]), int(self.ls[i][1]) + self.blank))

    def update(self):
        for i in range(3): 
            self.ls[i][0] -= self.speed
        #if self.ls[0][0] < 0
        if self.ls[0][0] < -self.width:
            self.ls.pop(0)
            x = self.ls[1][0] + self.distance
            y = 80
            self.ls.append([x,y])

class Score():
    def __init__(self):
        self.score = 0
        self.addScore = True
    
    def draw(self):
        font = pygame.font.SysFont('consolas', 40)
        scoreSuface = font.render(str(self.score), True, (0, 0, 0))
        textSize = scoreSuface.get_size()
        DISPLAYSURF.blit(scoreSuface, (int((WINDOWWIDTH - textSize[0])/2), 100))
    
    def update(self, bird, columns):
        collision = False
        for i in range(3):
            rectColumn = [columns.ls[i][0] + columns.width, columns.ls[i][1], 1, columns.blank]
            rectBird = [bird.x, bird.y, bird.width, bird.height]
            if rectCollision(rectBird, rectColumn) == True:
                collision = True
                break
        if collision == True:
            if self.addScore == True:
                self.score += 1
            self.addScore = False
        else:
            self.addScore = True
        
           

            

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Game cui bap')

def main():
    
    bird = Bird()
    column = Column()
    score = Score()
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
        score.draw()
        score.update(bird, column)
        if isGameOver(bird, column) == True:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()