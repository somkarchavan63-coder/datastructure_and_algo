import numpy as np
arr=np.array([1,2,4,5,6])
i=0
j=len(arr)-1
tar=6
while i<j:
    if arr[i]+arr[j]==tar:
        print(arr[i],arr[j])
        i=i+1
        j=j-1
    elif arr[i]+arr[j]>tar:
        j=j-1
    elif arr[i]+arr[j]<tar:
        i=i+1
    else:
        print("no element found")
