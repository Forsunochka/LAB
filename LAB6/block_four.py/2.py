massiv = [1,2,0,4]
print ("Начальный массив", massiv)

sred = sum(massiv)/len(massiv) if len(massiv)>0 else 0
print ("Среднее= ",sred)

for i in range(len(massiv)):
    if massiv[i]==0:
        massiv[i]=sred
        print ("Измененный массив", massiv)        