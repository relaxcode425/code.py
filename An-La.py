import numpy as np

lista=[]
lista=np.arange(1,101)

almacen=[]

ganancias=[0,0,0,0]

def mostrar():
    print(lista)


def comprar_asientos():

    print(lista)
    
    print("PLatinum, $120.000(asientos del 1 al 20)")
    
    print("Gold,$80.000 (asientos del 21 al 50)")
    
    print("silver,$50.000(asientos del 51 al 100)")
    
    opcion=int(input("Seleccione el asiento que desea comprar(asientos en 0 ocupados): "))
    
    cantidad=int(input("seleccione la cantidad (minimo 1 maximo 3): "))
    
    rut=int(input("Ingrese su rut(8 digitos, sin puntos ni guion):" ))
    
    if cantidad <1 and cantidad >3:
        print("cantidad invalida")
    
    if rut >8 and rut <8:
    
        print("rut invalido")
    
    if opcion>=1 and opcion <=20:

        #g = 1
        for x in ganancias:
            x[0] = int(x[0])+1
        
        precio=120000
    
    elif opcion>=21 and opcion<=50:
        
        #g = 2
        for x in ganancias:
            x[1] = int(x[1])+1
        
        precio=80000
        
    elif opcion>= 51 and opcion<=100:
        
        #g = 3
        for x in ganancias:
            x[2] = int(x[2])+1
        
        precio=50000
        
    else:
        
        print("Opcion fuera de rango") 
        
    #if g==1:
    
    #    ganancias[0] = (int(ganancias[0]))+1
    
    #elif g==2:
    
    #    ganancias[1] = (int(ganancias[1]))+1
    
    #elif g==3:
    
    #    ganancias[2] = (int(ganancias[2]))+1
    
    
    if lista[opcion-1]=='0':
        
        print("Ese asiento ya esta ocupado, por favor seleccione otro:")
        
    else:
        
        lista[opcion-1]='0'
        
        print("asiento comprado correctamente")
        
        total=precio
        
        print(f"total:${total}")
        
        print(lista)
        
        almacen.append(rut)


def listado():
    
    almacen.sort
    
    print(almacen)

def ganancias():
    
    print(ganancias)
    
    print(f"PLATINUM $120.000 {ganancias[0]}, TOTAL:{120.000*ganancias[0]}")
    
    print(f"GOLD $80.000 {ganancias[1]}, TOTAL:{80000*ganancias[1]}")
    
    print(f"SILVER $50000 {ganancias[2]}, TOTAL:{50000*ganancias[2]}")
    
    print(f"Subtotal{ganancias[0]+ganancias[1]+ganancias[2]}")
    
    #Error que no pude solucionar.


def salir():
    print("Adios antonio Lankin")


seleccion=0
while seleccion!=5:

    try:
    
        print("Menu de compra Creativos.cl")
        
        print("1.-Mostrar ubicaciones diponibles")
        
        print("2.-Comprar asientos")
        
        print("3.-Ver listado de asistentes")
        
        print("4.- Mostrar ganancias totales")
        
        print("5.-Salir")
        
        seleccion=int(input("Ingrese una opcion:"))
        
        if seleccion==1:
        
            mostrar()
        
        elif seleccion==2:
        
            comprar_asientos()
        
        elif seleccion==3:
        
            listado()
        
        elif seleccion==4:
        
            ganancias()
        
        elif seleccion==5:
        
            salir()
        
        else:
        
            print("Ingrese un valor valido")    
    except ValueError:
    
        print("error del sistema")