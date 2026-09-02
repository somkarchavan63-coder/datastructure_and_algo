s="abacdbefsab"
low=0
high=0
res=-1
k=4
freq={}
for high in range(len(s)):
    freq[s[high]]=freq.get(s[high],0)+1

    while len(freq)>k:
        freq[s[low]]=freq[s[low]]-1
        if freq[s[low]]==0:
            del freq[s[low]]
        low=low+1

    if len(freq)==k:
        len_=high-low+1
        res=max(res,len_)

print(res)