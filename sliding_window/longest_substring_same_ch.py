s="aabacbacab"
low=0
high=0
freq={}
res=-1
k=2

for high in range(len(s)):
    freq[s[high]]=freq.get(s[high],0)+1

    len_=high-low+1

    max_freq=max(freq.values())

    remain_freq=len_-max_freq

    while remain_freq>k:
        freq[s[low]]=freq[s[low]]-1
        low=low+1
        len_=high-low+1
        max_freq=max(freq.values())
        remain_freq=len_-max_freq

    len_=high-low+1
    res=max(res,len_)

print(res)

