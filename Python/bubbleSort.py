vet = [1,3,5,7,2,4,6]
dim=len(vet)
j=0
i=dim-1
for indice in reversed(range(i+1)):
    #print(indice)
    for j in range(indice):
        if vet[j]>vet[j+1]:
            temp=vet[j+1]
            vet[j+1]=vet[j]
            vet[j]=temp
print(vet)