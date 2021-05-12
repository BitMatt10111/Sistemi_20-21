#Author: Matteo Lamberti
#Target: make a program that find the fastest way to go from a to b

# stanza rettangolare con piastrelle e ostacoli
# (matrice 0 per piatrelle vuote - 1 per piastrelle occupate)
# il robot (verde) vuole andare in un punto (viola)
# calcolare il percorso più breve
# caricare un dizionario di posti in cui si può andare (dizionario delle adiacenze)

import pygame
import sys
import random
import time
INF=999999999999
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
                        temp.append((mat[i-1][k],random.randint(2,8)))
                if k != 0:
                    if mat[i][k-1]!=-1:
                        temp.append((mat[i][k-1],random.randint(2,8)))
                if i != len(mat)-1:
                    if mat[i+1][k]!=-1:
                        temp.append((mat[i+1][k],random.randint(2,8)))
                if k != len(mat[i])-1:
                    if mat[i][k+1]!=-1:
                        temp.append((mat[i][k+1],random.randint(2,8)))
                aD[mat[i][k]]=temp
    return aD             

def disegnaRobot(robotX,robotY):
    robot= pygame.Rect(robotY, robotX, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, GREEN, robot)  

def dijkstra(start,dizionario):
    label={}
    nodeList=[start]
    nodesEliminati=[]
    predecessori={}

    for nodo in dizionario:
        label[nodo]=INF
        predecessori[nodo]=None

    label[start]=0

    while len(nodeList) > 0:
        #cerco tra i nodi presenti in nodelist quello che ha la label più piccola
        #il nodo trovato sarà il nodo corrente
        #print(nodeList)
        nodeCorr=nodeList[0]
        for node in nodeList:
            if label[node]<label[nodeCorr]:
                nodeCorr=node
        #print(f"il nodo corrente è: {nodeCorr}")
        #trovo le adiacenze a partire dal nodo corrente - FOR
        #per ogni adiacenza calcolo la nuova label aggiornando il dizionario label solo se la label trovata
        #risulta piu piccola di quella gia trovata - FOR
        for nodesAdjT in dizionario[nodeCorr]:
            if not(nodesAdjT[0] in nodesEliminati) and not(nodesAdjT[0] in nodeList):
                nodeList.append(nodesAdjT[0])
            if label[nodeCorr]+nodesAdjT[1] < label[nodesAdjT[0]]:
                label[nodesAdjT[0]]=label[nodeCorr]+nodesAdjT[1]
                predecessori[nodesAdjT[0]]=nodeCorr
        nodeList.remove(nodeCorr)
        nodesEliminati.append(nodeCorr)
    return label,predecessori

def creaPercorso(preced,nE):
    nodeCorr=nE
    percorso=[]
    for _ in preced.keys():
        for key in preced.keys():
            if key==nodeCorr:
                percorso.append(nodeCorr)
                nodeCorr=preced[key]
    percorso.reverse()
    return percorso

def moveRobot(x,y,element,mat):  
    if mat[x-1][y]==element:
        x=x-1
    if mat[x][y-1]==element:           
        y=y-1
    if mat[x+1][y]==element:
        x=x+1
    if mat[x][y+1]==element:
        y=y+1
    return x,y

def main():
    mat = [[0,0,0,-1,-1],
        [-1,0,0,0,-1],
        [0,0,-1,-1,-1],
        [0,0,-1,0,0],
        [-1,0,0,0,0],
        [-1,-1,-1,0,0]]
    robotX=1
    robotY=3
    j=0
    nodeStart=5
    nodeEnd=8
    enumerateSlots(mat)
    aD=adjacencyDictionary(mat)
    print(aD)
    labels,predecessori = dijkstra(nodeStart,aD)
    percorso=creaPercorso(predecessori,nodeEnd)
    while True:
        creaGriglia(mat)
        disegnaRobot(robotX *CELL_SIZE,robotY*CELL_SIZE)
        time.sleep(1)
        if j<len(percorso):
            robotX,robotY=moveRobot(robotX,robotY,percorso[j],mat)
            j+=1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
    
if __name__ == "__main__":
    main()