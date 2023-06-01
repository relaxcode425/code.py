import os
acu = 0
L = []
for i in range(10):
    os.system("cls")
    print(f"{L}\n--------------------------------------------------------")
    n = int(input(f"ingrese el numero {i+1} de 10: "))
    L.append(n)
for i in L:
    acu = acu + i
print("suma: ",acu)
print("promedio: ",(acu/10))