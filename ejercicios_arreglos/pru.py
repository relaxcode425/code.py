import numpy as np
import os

list1 = []
for x in range(1,11):
    for y in range(1,5):
        list1.append(x)
arr1 = np.array(list1)
arr1 = arr1.reshape(40,1)

print(arr1)

list2 = []
for x in range(1,11):
    list2.append("A")
    list2.append("B")
    list2.append("C")
    list2.append("D")
arr2 = np.array(list2)
arr2 = arr2.reshape(40,1)
arr1 = np.concatenate((arr1,arr2),axis=1)

print(arr1)

list3 = []
for x in range():
    list3.append("")
arr3 = np.array

cont_num = 0
num = '1234567890'
codigo = input("se tiene que ingresar como: ABC123123")
for x in codigo:
    for y in num:
        if x == y:
            cont_num = cont_num + 1