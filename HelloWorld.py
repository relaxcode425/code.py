import os
opcion = 0
option = 0
cantnormal = 0
cantdeluxe = 0
cantcollector = 0
cant = 0
total = 0
descuento = 0
while opcion != 6:
    try:
        descuento = 0
        print("Menu de Compra\n\t1.-Normal Edition\n\t2.-Deluxe Edition\n\t3.-Collector Edition\n\t4.-Siguiente\n\t5.-Cancelar compra\n\t6.-Salir\n-------------------------------------")
        if cantcollector > 0:
            print(f"*       {cantcollector} Collector Edition   ${cantcollector*150000}")
        if cantdeluxe > 0:
            print(f"*       {cantdeluxe} Deluxe Edition   ${cantdeluxe*72000}")
        if cantnormal > 0:
            print(f"*       {cantnormal} Normal Edition   ${cantnormal*55000}")
        opcion = int(input())
        os.system("cls")
        if opcion == 1 or opcion == 2 or opcion == 3:
            cant = int(input("ingrese la cantidad que desea comprar: "))
            os.system("cls")
            if cant > 0:
                if opcion == 1:
                    cantnormal = cantnormal + cant
                    total = total + (cant*55000)
                elif opcion == 2:
                    cantdeluxe = cantdeluxe + cant
                    total = total + (cant*72000)
                elif opcion == 3:
                    cantcollector = cantcollector + cant
                    total = total + (cant*150000)
            else:
                os.system("cls")
                input("numero invalido...")
        elif opcion == 4:
            print("seleccione su tarjta de pago:\n\t1.-Tarjeta CMR\n\t2.-Tarjeta BCI\n\t3.-Tarjeta Pato Estado\n\t4.-Otro...\n\t5.-Cancelar compra")
            option = int(input())
            os.system("cls")
            if option == 1:
                descuento = 0.15
            elif option == 2:
                descuento = 0.23
            elif option == 3:
                descuento = 0.08
            elif option == 4:
                input("ingrese nombre de su tarjeta: ")
            elif option == 5:
                cantnormal = 0
                cantdeluxe = 0
                cantcollector = 0
                total = 0
            else:
                os.system("cls")
                input("vuelva a intentar con la opcion: Siguiente...")
            if option > 0 and option <5:
                os.system("cls")
                print("Compra Realizada\n-------------------------------------")
                if cantcollector > 0:
                    print(f"*       {cantcollector} Collector Edition   ${cantcollector*150000}")
                if cantdeluxe > 0:
                    print(f"*       {cantdeluxe} Deluxe Edition   ${cantdeluxe*72000}")
                if cantnormal > 0:
                    print(f"*       {cantnormal} Normal Edition   ${cantnormal*55000}")
                print(f"-------------------------------------\nSubtotal                 ${total}\nDescuento {descuento*100}%      ${total*descuento}\n-------------------------------------\nTotal a pagar        ${total-(total*descuento)}")
                input(" ")
                os.system("cls")
                cantnormal = 0
                cantdeluxe = 0
                cantcollector = 0
                total = 0
        elif opcion == 5:
            cantnormal = 0
            cantdeluxe = 0
            cantcollector = 0
            total = 0
        elif opcion == 6:
            cantnormal = 0
            cantdeluxe = 0
            cantcollector = 0
            total = 0
        else:
            os.system("cls")
            input("ingrese una opcion valida...")
    except ValueError:
        os.system("cls")
        input("ingrese un valor correcto...")
    except:
        os.system("cls")
        input("error de sistema...")