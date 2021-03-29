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

#PER VEDERE BENE I GRAFICI:
#commentare quelli che non si desidera vedere ed inserire quelli da visualizzare qua sotto (Max: 2 o 3 )
fig, (ax5) = plt.subplots(1,1)
fig.suptitle("Plots")
'''
ax1.plot(total,anomalies, ".g")
ax1.set_xlabel("Total (Million tons)")
ax1.set_ylabel("Anomalies\n(°C)")

ax2.plot(gasFuel,anomalies, ".r")
ax2.set_xlabel("Gas Fuel (Million tons)")
ax2.set_ylabel("Anomalies\n(°C)")

ax3.plot(liquidFuel,anomalies, ".c")
ax3.set_xlabel("Liquid Fuel (Million Tons)")
ax3.set_ylabel("Anomalies\n(°C)")

ax4.plot(solidFuel,anomalies, ".b")
ax4.set_xlabel("Solid Fuel (Million Tons)")
ax4.set_ylabel("Anomalies\n(°C)")
'''
ax5.plot(cement,anomalies, ".g")
ax5.set_xlabel("Cement (Million Tons)")
ax5.set_ylabel("Anomalies\n(°C)")
'''
ax6.plot(gasFlaring,anomalies, ".k")
ax6.set_xlabel("Gas Flaring (Million Tons)")
ax6.set_ylabel("Anomalies\n(°C)")

ax7.plot(perCapita,anomalies, ".r")
ax7.set_xlabel("Per Capita (Total emission/Total popolation)\n(Only >= 1950)")
ax7.set_ylabel("Anomalies\n(°C)")
'''
plt.show()