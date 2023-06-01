import os
os.system("cls")
hoa = [60, 512, 22, [1, 2, 3]]
print("listra dentro de lista: [",hoa[3][0], hoa[3][2], "]\n")

#lista2
lista2 = [24, 13, 75, 85]
print("lista 2: ", lista2)

#agregar elementos al final de la lista:
lista2.append((90))
print("append:  ", lista2)

#agregar los elementos de una lista al final de otra:
lista_extend = [169, 42, 5]
lista2.extend(lista_extend)
print("extend:  ", lista2)

#agregar un valor en la posicion indicada (primero va la posicion):
lista2.insert(0, 3)
print("insert:  ", lista2)

#remover un el valor indicado de la lista:
lista2.remove(3)
print("remove:  ", lista2)

#remover un valor segun la posicion indicada (si no se indica, elimina el valor de la ultima posicion):
lista2.pop(-2)
print("pop:     ", lista2)

#invertir el orden de la lista:
lista2.reverse()
print("reverse: ", lista2)
lista2.reverse()

#ordena de menor a mayor:
lista2.sort()
print("sort:    ", lista2)

#ordena de mayor a menor:
lista2.sort(reverse=True)
print("sort 2:  ", lista2)