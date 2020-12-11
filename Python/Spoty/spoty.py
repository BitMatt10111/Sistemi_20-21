file = open("canzoni.csv","r")
playlist = []
dizTemp = {}
for riga in file:
    if(riga[-1]=="\n"):
        rigaTemp = riga[0:-1].split(",")
    else:
        rigaTemp = riga.split(",")
    dizTemp["indice"]=rigaTemp[0]
    dizTemp["titolo"]=rigaTemp[1]
    dizTemp["autore"]=rigaTemp[2]
    dizTemp_copy = dizTemp.copy()
    playlist.append(dizTemp_copy)

for x in playlist:
    print(x["indice"],x["titolo"],x["autore"])
    