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


asientos[11,1] = "full"

print(asientos)









def verasientos():
    ver = []
    for x in asientos:
        if x[1] == "free":
            ver.append(x[0])
        elif x[1] == "full":
            ver.append("x")
    ver = np.array(ver)
    ver = ver.reshape(14,3)
    return ver
print(verasientos())