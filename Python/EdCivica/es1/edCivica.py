import matplotlib.pyplot as plt
import csv

numMesi=[]
mediaTemp=[]
giaccaDays=[]
scuolaDays=[]
videogamesDays=[]
dataFile = open("csv.csv","r")
dataReader = csv.reader(dataFile,delimiter=",")
next(dataReader)
for row in dataReader:
    numMesi.append(int(row[1]))
    mediaTemp.append(float(row[2]))
    giaccaDays.append(int(row[3]))
    scuolaDays.append(int(row[4]))
    videogamesDays.append(int(row[5]))

fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1)
fig.suptitle("Plot")

ax1.plot(numMesi,mediaTemp, "o-g")
ax1.set_xlabel("Mese")
ax1.set_ylabel("Temperatura")

ax2.plot(numMesi,giaccaDays, "o-r")
ax2.set_xlabel("Mese")
ax2.set_ylabel("Giacca")

ax3.plot(numMesi,scuolaDays, "o-c")
ax3.set_xlabel("Mese")
ax3.set_ylabel("Scuola")

ax4.plot(numMesi,videogamesDays, "o-m")
ax4.set_xlabel("Mese")
ax4.set_ylabel("Videogiochi")

plt.show()