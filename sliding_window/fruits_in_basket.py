import numpy as np

arr=np.array([1,2,1,3,2,4,3])

low=0
high=0
res=-1
k=2
freq={}

for high in range(len(arr)):
    freq[arr[high]]=freq.get(arr[high],0)+1

    while len(freq)>k:
        freq[arr[low]]=freq[arr[low]]-1
        if freq[arr[low]]==0:
            del freq[arr[low]]
        low=low+1

    if len(freq)==k:
        len_=high-low+1
        res=max(res,len_)

print(res)