def maxAnomalia(anno1,anno2):
    file = open("annual.csv","r")
    finalMax=0.0
    finalMin=0.0
    if(anno2<anno1):
        anno2,anno1=anno1,anno2
    for k,riga in enumerate(file):
        if(k>0):
            rigaTemp = riga[0:-1].split(",")
            _=rigaTemp[0]
            anno=int(rigaTemp[1])
            temp=float(rigaTemp[2])
            if(anno>=anno1 and anno<=anno2):
                if(anno==anno2):
                    finalMax=temp
                    finalMin=temp
                else:
                    if(temp>finalMax):
                        finalMax=temp
                    if(temp<finalMin):
                        finalMin=temp
    return finalMin,finalMax

file = open("annual.csv","r")
diz={}
for k,riga in enumerate(file):
    if(k>0):
        rigaTemp = riga[0:-1].split(",")
        fonte=rigaTemp[0]
        anno=rigaTemp[1]
        temp=rigaTemp[2]
        if(k%2==0):
            diz[anno]+=float(temp)
            diz[anno]=float(diz[anno])/2
        else:
            diz[anno]=float(temp)

print(diz["1990"],diz["2000"],diz["2010"])
print(maxAnomalia(2016,2010))