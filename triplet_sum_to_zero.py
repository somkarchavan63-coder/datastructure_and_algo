import numpy as np

arr=np.array([-1,0,0,1,1,])

i=0
j=i+1
k=len(arr)-1

arr_len=len(arr)
result=[]
for i in range(arr_len-2):
    j=i+1
    k=len(arr)-1
    sum=-1*arr[i]
    s=arr[j]+arr[k]
    if arr[i]==arr[i-1]:
        continue
    while j<k:
        if s==sum:
            result.append([int(arr[i]),int(arr[j]),int(arr[k])])
            j=j+1
            k=k-1
        elif s>sum:
            k=k-1
        elif s<sum:
            j=j+1
        else:
            print("values not found")

        if j<arr_len and arr[j]==arr[j-1]:
            j=j+1
        if k>=0 and arr[k]==arr[k+1]:
            k=k-1

print(result)