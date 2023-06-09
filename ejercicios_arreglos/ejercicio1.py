import random
import numpy as np

arr = np.random.randint(0,500,(100))
arr.sort()
print(arr)

for i in range(0,50):
    print(arr[i*2])