import numpy as np

arr=np.array([2,1,3,4,5,2,6])
target=6
sum=0
s=float('inf')
low=0
high=0
while high<=len(arr)-1:
    sum=sum+arr[high]
    while sum>=target:
        diff=high-low+1
        s=min(s,diff)

        sum=sum-arr[low]
        low=low+1
    high=high+1

print(s)
