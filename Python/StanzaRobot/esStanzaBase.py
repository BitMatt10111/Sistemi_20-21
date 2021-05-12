#Author: Matteo Lamberti
#Target: make a program that find the fastest way to go from a to b

# stanza rettangolare con piastrelle e ostacoli
# (matrice 0 per piatrelle vuote - 1 per piastrelle occupate)
# il robot (verde) vuole andare in un punto (viola)
# calcolare il percorso più breve
# caricare un dizionario di posti in cui si può andare (dizionario delle adiacenze)

import pygame
import sys
CELL_SIZE = 100
BLACK = (0,0,0) #RGB
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,0,255)

def creaGriglia(mat):
    global screen
    pygame.init()
    i=0
    k=0
    contCelle=0
    dimension=(CELL_SIZE*len(mat[0]),CELL_SIZE*len(mat))
    screen = pygame.display.set_mode(dimension)
    screen.fill(BLACK)
    for y in range(0,dimension[1],CELL_SIZE):
        for x in range(0,dimension[0],CELL_SIZE):
            tile = pygame.Rect(x,y,CELL_SIZE,CELL_SIZE)
            if mat[i][k]==-1:
                pygame.draw.rect(screen,RED,tile)
            else:
                pygame.draw.rect(screen,WHITE,tile,1)
                fnt = pygame.font.SysFont(None, 25, bold = True)
                txt = fnt.render(str(contCelle), True, (255, 255, 255))
                screen.blit(txt, (x+10, y+10))
                contCelle+=1
            k+=1
        k=0
        i+=1

def enumerateSlots(mat):
    n=0
    i=0
    for row in mat:
        k=0
        for value in row:
            if value==0:
                mat[i][k]=n
                n+=1
            k+=1
        i+=1

def adjacencyDictionary(mat):
    aD={}
    for i in range(0,len(mat)): #y - row
        for k in range(0,len(mat[0])):  #x - column
            if mat[i][k]!=-1:
                temp=[]
                if i != 0:
                    if mat[i-1][k]!=-1:
                        temp.append(mat[i-1][k])
                if k != 0:
                    if mat[i][k-1]!=-1:
                        temp.append(mat[i][k-1])
                if i != len(mat)-1:
                    if mat[i+1][k]!=-1:
                        temp.append(mat[i+1][k])
                if k != len(mat[i])-1:
                    if mat[i][k+1]!=-1:
                        temp.append(mat[i][k+1])
                aD[mat[i][k]]=temp
    return aD             

def disegnaRobot(robotX,robotY):
    robot= pygame.Rect(robotY, robotX, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, GREEN, robot)  

def main():
    mat = [[0,0,0,-1,-1],
        [-1,0,0,0,-1],
        [0,0,-1,-1,-1],
        [0,0,-1,0,0],
        [-1,0,0,0,0],
        [-1,-1,-1,0,0]]
    robotX=0
    robotY=0
    enumerateSlots(mat)
    aD=adjacencyDictionary(mat)
    while True:
        creaGriglia(mat)
        disegnaRobot(robotX *CELL_SIZE,robotY*CELL_SIZE)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if robotX-1>-1:    
                    if event.key == pygame.K_w and mat[robotX-1][robotY]!=-1:
                        robotX=robotX-1
                if robotY-1>-1:    
                    if event.key == pygame.K_a and mat[robotX][robotY-1]!=-1:           
                        robotY=robotY-1
                if robotX+1<=5:  
                    if event.key == pygame.K_s and mat[robotX+1][robotY]!=-1:
                        robotX=robotX+1
                if robotY+1<=4:
                    if event.key == pygame.K_d and mat[robotX][robotY+1]!=-1:
                        robotY=robotY+1
        pygame.display.update()
    
if __name__ == "__main__":
    main()