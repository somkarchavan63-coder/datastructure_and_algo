####given two string s and t of the length m and n ,return the min window of s which consisit the all elemnets of the t including duplicates also
"""s="aabcbcaccabb"
t="abc"
low=0
high=0
freq_s={}
freq_t={}
have=0
min_len=float('inf')
result=""
for high in range(len(t)):
    freq_t[t[high]]=freq_t.get(t[high],0)+1

for high in range(len(s)):
    ch=s[high]
    freq_s[ch]=freq_s.get(ch,0)+1
    len_freq_t=len(freq_t)

    if ch in freq_t and freq_s[ch]==freq_t[ch]:
        have=have+1

    while have==len_freq_t:
        if high-low+1<min_len:
            min_len=high-low+1
            result=s[low:high+1]

        left_ch=s[low]
        freq_s[left_ch]=freq_s[left_ch]-1

        if left_ch in freq_t and freq_s[left_ch]<freq_t[left_ch]:
            have=have-1
        low=low+1
        

    
    
print(result)"""

s="aabacsbacabcdbaab"
t="bacsa"
low=0
high=0
result=""
freq_s={}
freq_t={}
have=0
min_len=float('inf')

for high in range(len(t)):
    freq_t[t[high]]=freq_t.get(t[high],0)+1

for high in range(len(s)):
    ch=s[high]
    freq_s[ch]=freq_s.get(ch,0)+1

    if ch in freq_t and freq_s[ch]==freq_t[ch]:
        have=have+1

    while have==len(freq_t):
        if high-low+1<min_len:
            min_len=high-low+1
            result=s[low:high+1]

        ch=s[low]
        freq_s[ch]=freq_s[ch]-1

        if ch in freq_t and freq_s[ch]<freq_t[ch]:
            have=have-1

        low=low+1

print(result)


