import numpy as np
"""arr=np.array([1,2,2,3,2,4,5])
freq={}
for num in arr:
    freq[int(num)]=freq.get(int(num),0)+1

print(freq)"""

s="aabbcadfbb"
low=0
high=0
k=3
freq={}
res=-1
while high<len(s):
    freq[s[high]]=freq.get(s[high],0)+1

    while len(freq)>k:
        freq[s[low]]=freq[s[low]]-1
        if freq[s[low]]==0:
            del freq[s[low]]
        low=low+1

    if len(freq)==k:
        len_=high-low+1
        res=max(res,len_)
    high=high+1
print(freq)
print(res)
