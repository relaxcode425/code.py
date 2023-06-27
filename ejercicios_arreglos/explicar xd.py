import numpy as np
import os

arr = np.arange(1,43)
arr = arr.reshape(42,1)
list2 = []
for x in range(1,43):
    list2.append("free")
arr2 = np.array(list2)
arr2 = arr2.reshape(42,1)
asientos = np.concatenate((arr,arr2),axis=1)

list3 = []
for x in range(1,211):
    list3.append("-")
arr3 = np.array(list3)
arr3 = arr3.reshape(42,5)
asientos = np.concatenate((asientos,arr3),axis=1)
#print(asientos)
asientos[9,1] = "full"
#print(asientos)


def verasientos():
    ver = []
    for x in asientos:
        if x[1] == "free":
            ver.append(x[0])
        elif x[1] != "free":
            ver.append("x")
    ver = np.array(ver)
    ver = ver.reshape(14,3)
    return ver

#print(verasientos())
def comprar():
    precio = 0
    cont = 0
    check = False
    while check == False:
        os.system("cls")
        print("ingrese 1 si desea cancelar, ingrese 0 para continuar...")
        opcion = int(input())
        os.system("cls")
        if opcion == 1:
            check = True
        else:
            nombre = "-"
            rut = "-"
            telefono = "-"
            banco = "-"
            puesto = 0
            nombre = input("ingrese el nombre completo del pasajero: ")
            rut = input("ingrese el RUT del pasajero (CON guion, SIN puntos): ")
            if len(rut) < 11 and len(rut) > 8:
                telefono = input("ingrese el numero de telefono del pasajero: ")
                if len(telefono) < 10 and len(telefono) > 8: 
                    banco = input("ingrese su banco: ")
                    if banco == "BANCO DUOC" or banco == "BANCODUOC" or banco == "banco duoc" or banco == "bancoduoc":
                        descuento = True
                    else:
                        descuento = False
                    os.system("cls")
                    print(verasientos())
                    puesto = int(input("ingrese el asiento que desea comprar: "))
                    os.system("cls")
                    if puesto > 0 and puesto < 43:
                        for x in asientos:
                            if int(x[0]) == puesto:
                                if x[1] == "full":
                                    puesto = 0
                                    input("ingrese un puesto valido...")
                                else:
                                    check = True
                    else:
                        input("ingrese un puesto valido...")
                else:
                    print("ingrese un numero de telefono valido")
            else:
                input("ingrese un rut valido...")
    for x in asientos:
        if int(x[0]) == puesto:
            x[1] = "full"
            x[2] = nombre
            x[3] = rut
            x[4] = telefono
            x[5] = banco
            if int(x[0]) >= 31:
                precio = 240000
            elif int(x[0]) < 31:
                precio = 78900
            if descuento == True:
                precio = precio * 0.85
            x[6] = precio
            os.system("cls")
            if descuento == True:
                print(f"tiene un descuento de 15%")
            input(f"su compra tiene el valor de ${precio}...")
comprar()
print(verasientos())