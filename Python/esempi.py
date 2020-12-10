stringa = "ciao"
f=5.6
variabile_intera = 7
print(f"il valore è: {variabile_intera}")

#collezioni: liste, tuple, dizionari

#liste
lamialista = [0,1,2,3,4,"ciao","babbo"] #anche tipi diversi
print(lamialista)

cnt=0
for elemento in enumerate(lamialista):
    print(f"L'elemento {cnt+1}esimo è: {elemento}")
    cnt = cnt + 1

a=5
b=3
b ,a = a ,b #scambiale variabili

import random #include la libreria random

v=[] #lista vuota
for num in range(0,10):
    v.append(random.randint(0,100)) #append aggiunge un elemento alla lista

def caio(vet,x): #definizione di funzione
    x=5
    vet["ciao","banana","pesce"]
    print(vet)

v[:7] #tutto fino alla cella 7
v[3:] #tutto partendo da 3
v[3:7] #tutto da 3 a 7 escluso

#tipi di for
for x in [3,4,1,8]:
    print(x);

lista = [3,4,1,8]
for i in range(0,len(lista),1):
    print(lista[i])

for i, element in enumerate(lista):
    print(f"indice: {i} - elemento: {elemento}")

#dizionario
canzone = {"numero":1,"titolo":"20 anni","autore":"Maneskin"}
print(canzone["autore"])#uso la chiave "autore" per fargli stampare "Maneskin"

elenco_classe = {1:"Alladio",2:"Alpigiano",3:"Bertoglio"}
print(canzone[2])#uso la chiave 2 per fargli stampare "Alpigiano"

#si possono anche fare liste di dizionari[{}] e dizionari di liste{[]}