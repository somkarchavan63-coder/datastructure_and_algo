import numpy as np

arr=np.array([1,3,5,7,2,6,9])
#window size=2
k=2
low=0
high=k-1
sum=0
res=0
for i in range(high+1):
    sum=sum+arr[i]
print(sum)
while high<len(arr):
    res=max(res,sum)

    low=low+1
    high=high+1
    if high==len(arr):
        break
    sum=sum-arr[low-1]+arr[high]

print(res)
        




