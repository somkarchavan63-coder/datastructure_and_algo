import numpy as np

arr=np.array([1,1,2,3,3,4,5,5])

i=0
j=i+1
while i<len(arr)-1:
    if arr[i]==arr[j]:
        arr=np.delete(arr,j)
        j=j+1
    else:
        i=j
        j=j+1
print(arr)