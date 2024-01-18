import os
from tabulate import tabulate
os.system('cls')
equipos = [['A',9],['B',2],['c',1],['d',0]]
orden = equipos.sort()
for i,item in enumerate(equipos):
    for j in range(int(i+1),len(equipos),1):
        if(equipos[i][1] > equipos[j][1]):
            aux = equipos[i]
            equipos[i]= equipos[j]
            equipos[j] = aux
print(tabulate(equipos,headers=['Equipo','PJ','PG'],tablefmt='grid'))