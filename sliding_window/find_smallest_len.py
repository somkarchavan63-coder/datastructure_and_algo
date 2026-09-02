###finding the smallest len of array whi9ch satisfy the condition
import numpy as np
arr=np.array([30,40,50,86,20,30,70])
low=0
high=0
res=float('inf')
##condtion sum>85 
tar=85
sum=0
for high in range(len(arr)):
    sum=sum+arr[high]
    while sum>tar:
        len_=high-low+1
        res=min(res,len_)
        sum=sum-arr[low]
        low=low+1

print(res)
        

