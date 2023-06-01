import os
L = []
n = 1
while n != 0:
    os.system("cls")
    L.sort()
    print(L, "\n---------------")
    n = int(input("ingrese numeros que desea ordenar (0 para terminar): "))
    if n != 0:
        L.append(n)
os.system("cls")
print(L)