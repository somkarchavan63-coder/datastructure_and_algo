import numpy as np

arr=np.array([1,0,2,1,0,1,2,1,2,2,0,1,2,0])
low=0
mid=0
high=len(arr)-1
temp=0
while mid<=high:
    if arr[mid]==0:
        temp=arr[low]
        arr[low]=arr[mid]
        arr[mid]=temp
        low=low+1
        mid=mid+1
    elif arr[mid]==2:
        temp=arr[mid]
        arr[mid]=arr[high]
        arr[high]=temp
        high=high-1
    else:
        mid=mid+1
print(arr)
        