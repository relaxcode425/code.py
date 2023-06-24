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
            asientos[cont,1] = "full"
            asientos[cont,2] = nombre
            asientos[cont,3] = rut
            asientos[cont,4] = telefono
            asientos[cont,5] = banco
            if cont+1 >= 31:
                precio = 240000
            elif cont+1 < 31:
                precio = 78900
            if descuento == True:
                precio = precio * 0.85
            x[6] = precio
            os.system("cls")
            if descuento == True:
                print(f"tiene un descuento de 15%")
            input(f"su compra tiene el valor de ${precio}...")
        cont = cont+1

def anularasiento():
    os.system("cls")
    print("para anular su compra se necesita del asiento y el rut del pasajero...")
    opc = int(input("para seguir con este tramite ingrese 1, en caso contrario ingrese 0..."))
    while opc == 1:
        os.system("cls")
        lugar = int(input("ingrese el asiento: "))
        rut = input("ingrese el rut del pasajero: ")
        os.system("cls")
        find = False
        for x in asientos:
            if int(x[0]) == lugar and x[3] == rut:
                find = True
                print(f"el nombre del pasajero es: {x[2]}, ¿es esto correcto?")
                confirmacion = int(input("1- si\n2- no\n"))
                os.system("cls")
                if confirmacion == 1:
                    print(f"se le devolverá el precio cancelado por el asiento: ${x[6]}")
                    x[1] = "free"
                    x[2] = "-"
                    x[3] = "-"
                    x[4] = "-"
                    x[5] = "-"
                    x[6] = "-"
                    input("el asiento ha sido liberado...")
                    os.system("cls")
        if find == True:
            os.system("cls")
            opc = int(input("si desea volver a intentar ingrese 1, de lo contrario ingrese 0: "))
        else:
            os.system("cls")
            input("los datos no coinciden...")
            opc = int(input("si desea volver a intentar ingrese 1, de lo contrario ingrese 0: "))

def modificardatos():
    os.system("cls")
    print("para modificar los datos del pasajero se necesita el asiento y rut de este\n(solo pueden ser cambiados el nombre y telefono del pasajero)")
    opc = int(input("para seguir con este tramite ingrese 1, en caso contrario ingrese 0..."))
    
    while opc == 1:
        os.system("cls")
        lugar = int(input("ingrese el asiento: "))
        rut = input("ingrese el rut del pasajero: ")
        os.system("cls")
        find = False
        for x in asientos:
            if int(x[0]) == lugar and x[3] == rut:
                find = True
                print(f"el nombre del pasajero es: {x[2]}, ¿es esto correcto?")
                confirmacion = int(input("1- si\n2- no\n"))
                os.system("cls")
                if confirmacion == 1:
                    confirmacion2 = int(input("¿desea cambiar el nombre del pasajero?\n1.- si\n2.- no\n"))
                    os.system("cls")
                    if confirmacion2 == 1:
                        print(f"el nombre registrado del pasajero es: {x[2]}")
                        nombre = input("ingrese el nombre por el cual lo desea reemplazar: ")
                        os.system("cls")
                        x[2] = nombre
                    confirmacion3 = int(input("¿desea cambiar el telefono del pasajero?\n1.- si\n2.- no\n"))
                    os.system("cls")
                    if confirmacion3 == 1:
                        print(f"el telefono registrado del pasajero es: {x[4]}")
                        telefono = input("ingrese el telefono por el cual lo desea reemplazar: ")
                        os.system("cls")
                        x[2] = telefono
                    if confirmacion2 == 1 or confirmacion3 == 1:
                        input("cambios realizados...")
                        os.system("cls")
                    else:
                        input("cambios cancelados...")
                        os.system("cls")
        if find == True:
            opc = int(input("si desea volver a intentar ingrese 1, de lo contrario ingrese 0: "))
            os.system("cls")
        else:
            input("los datos no coinciden...")
            opc = int(input("si desea volver a intentar ingrese 1, de lo contrario ingrese 0: "))
            os.system("cls")

eleccion = 0
while eleccion != 5:
    os.system("cls")
    eleccion = int(input("Seleccione una opcion:\n1.- ver asientos disponibles\n2.- comprar asiento\n3.- anular vuelo\n4.- modificar datos del pasajero\n5.- salir\n"))
    os.system("cls")
    try:
        if eleccion == 1:
            print(verasientos())
            input("...")
        elif eleccion == 2:
            comprar()
        elif eleccion == 3:
            anularasiento()
        elif eleccion == 4:
            modificardatos()
        elif eleccion == 5:
            input("adios...")
        else:
            input("ingrese un valor valido...")
    except ValueError:
        input("ingrese numeros o caracteres donde corresponda...")
    except:
        input("error del sistema...")