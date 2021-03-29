import matplotlib.pyplot as plt
import csv
MIN_ANNO=1880
MAX_ANNO=2010

year=[]
anomalies=[]
dataFile = open("Temperature_Anomaly.csv","r")
dataReader = csv.reader(dataFile,delimiter=",")
for _ in range(5): next(dataReader)
for row in dataReader:
    if int(row[0]) >= MIN_ANNO and int(row[0]) <= MAX_ANNO:
        year.append(int(row[0]))
        anomalies.append(float(row[1]))

total=[]
gasFuel=[]
liquidFuel=[]
solidFuel=[]
cement=[]
gasFlaring=[]
perCapita=[]
dataFile = open("CO2_emissions.csv","r")
dataReader = csv.reader(dataFile,delimiter=",")
next(dataReader)
for row in dataReader:
    if int(row[0]) >= MIN_ANNO and int(row[0]) <= MAX_ANNO:
        total.append(int(row[1]))
        gasFuel.append(int(row[2]))
        liquidFuel.append(int(row[3]))
        solidFuel.append(int(row[4]))
        cement.append(int(row[5]))
        gasFlaring.append(int(row[6]))
        if not row[7]:
            perCapita.append(-1.0)
        else:
            perCapita.append(float(row[7]))

fig, (ax1,ax2,ax5,ax6) = plt.subplots(4,1)
fig.suptitle("Plots")

ax1.plot(year,anomalies, "-g")
ax1.set_xlabel("Anni")
ax1.set_ylabel("Anomalies\n(°C)")
ax1.set_ylim([-0.5,2])

ax2.plot(year,total, "-r")
ax2.set_xlabel("Anni")
ax2.set_ylabel("Total\n(Million tons)\n \n \n")
'''
ax3.plot(year,gasFuel, "-c")
ax3.set_xlabel("Anni")
ax3.set_ylabel("Gas Fuel\n(Million tons)")

ax4.plot(year,liquidFuel, "-b")
ax4.set_xlabel("Anni")
ax4.set_ylabel("Liquid Fuel\n(Million tons)\n \n \n")
'''
ax5.plot(year,solidFuel, "-g")
ax5.set_xlabel("Anni")
ax5.set_ylabel("Solid Fuel\n(Million tons)")

ax6.plot(year,cement, "-k")
ax6.set_xlabel("Anni")
ax6.set_ylabel("Cement\n(Million tons)\n \n \n")
'''
ax7.plot(year,gasFlaring, "-r")
ax7.set_xlabel("Anni")
ax7.set_ylabel("Gas Flaring\n(Million tons)")

ax8.plot(year,perCapita, "-m")
ax8.set_xlabel("Anni")
ax8.set_ylabel("Per Capita\n(Total emission/\nTotal popolation)\n(Only >= 1950)\n \n \n")
'''

plt.show()