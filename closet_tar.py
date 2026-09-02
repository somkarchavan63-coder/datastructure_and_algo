import numpy as np
arr1=np.array([-1,0,1,2,3,4,5])
tar=5
min_diff=float('inf')
result_sum=0
for i in range(len(arr1)-2):
    j=i+1
    k=len(arr1)-1
    while j<k:
        sum=arr1[i]+arr1[j]+arr1[k]
        diff=abs(tar-sum)
        if min_diff>diff:
            min_diff=diff
            result_sum=sum
        if sum==tar:
            j=j+1
            k=k-1
        elif sum<tar:
            j=j+1
        else:
            k=k-1

print(result_sum)


