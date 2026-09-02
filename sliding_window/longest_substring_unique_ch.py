s="absfcasdcaba"
low=0
high=0
freq={}
l=[]
res=-1
for high in range(len(s)):
    freq[s[high]]=freq.get(s[high],0)+1

    k=high-low+1
    while len(freq)<k:
        freq[s[low]]=freq[s[low]]-1
        if freq[s[low]]==0:
            del freq[s[low]]
        low=low+1
        k=high-low+1

    len_=high-low
    res=max(res,len_)

print(res)



