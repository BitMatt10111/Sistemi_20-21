#Author: Matteo Lamberti
#Target: make a program that find the fastest way to go from a to b

# stanza rettangolare con piastrelle e ostacoli
# (matrice 0 per piatrelle vuote - 1 per piastrelle occupate)
# il robot (verde) vuole andare in un punto (viola)
# calcolare il percorso più breve
# caricare un dizionario di posti in cui si può andare (dizionario delle adiacenze)

#numerare le celle libere

import pygame
import sys
CELL_SIZE = 100
BLACK = (0,0,0) #RGB
WHITE = (255,255,255)
RED = (255,0,0)

def creaGriglia(mat):
    global screen
    pygame.init()
    i=0
    k=0
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

def main():
    mat = [[0,0,0,-1,-1],
        [-1,0,0,0,-1],
        [0,0,-1,-1,-1],
        [0,0,-1,0,0],
        [-1,0,-1,0,0],
        [-1,-1,-1,0,0]]
    enumerateSlots(mat)
    print(adjacencyDictionary(mat))
    while True:
        creaGriglia(mat)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
if __name__ == "__main__":
    main()
    