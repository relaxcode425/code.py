import numpy as np

total = 0
arr = np.arange(1,43)
arr = arr.reshape(42,1)
list2 = []
for x in range(1,43):
    list2.append("free")
arr2 = np.array(list2)
arr2 = arr2.reshape(42,1)
asientos = np.concatenate((arr,arr2),axis=1)

list3 = []
for x in range(1,169):
    list3.append("-")
arr3 = np.array(list3)
arr3 = arr3.reshape(42,4)
asientos = np.concatenate((asientos,arr3),axis=1)

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

def comprar():
    cont = 0
    nombre = input("ingrese el nombre completo del pasajero: ")
    rut = input("ingrese el RUT del pasajero (CON guion, SIN puntos): ")
    if len(rut) <11 and len(rut) > 8:
        telefono = input("ingrese el numero de telefono del pasajero: ")
        banco = input("ingrese su banco: ")
        print(verasientos())
        puesto = input("ingrese el asiento que desea comprar: ")
    else:
        input("ingrese un rut valido...")
    for x in asientos:
        if x[0] == puesto:
            asientos[cont,1] = "full"
            asientos[cont,2] = nombre
            asientos[cont,3] = rut
            asientos[cont,4] = telefono
            asientos[cont,5] = banco
            if cont+1 >= 31:
                precio = 240000
                return precio
            elif cont+1 < 31:
                precio = 78900
                return precio
        cont = cont+1
total = total + comprar()
print(total)





#if banco.upper == "BANCO DUOC" or banco.upper == "BANCODUOC":
#        descuento = True
#    else:
#        descuento = False