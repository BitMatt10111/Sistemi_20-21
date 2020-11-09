vet = [1,3,5,7,2,4,6]
dim=len(vet)
for i in range(dim-1):
    #print(indice)
    for j in range(dim-i-1):
        if vet[j]>vet[j+1]:
            vet[j],vet[j+1]=vet[j+1],vet[j]
print(vet)
