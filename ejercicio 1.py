import os
os.system("cls")
cont = 1
L = []
N = int(input("ingrese un numero para mostrar su tabla del 1 hasta el 10: "))
for i in range(10):
    L.append(N*cont)
    cont = cont+1
print(L)