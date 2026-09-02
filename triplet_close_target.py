import numpy as np

arr=np.array([1,3,4,5,7,9])
tar=7
max_diff=float('inf')
arr_len=len(arr)
for i in range(arr_len-2):
    j=i+1
    k=arr_len-1
    while j<k:
        sum=arr[i]+arr[j]+arr[k]
        diff=abs(tar-sum)
        if max_diff>diff:
            max_diff=diff
            result_sum=sum

        if sum==tar:
            j=j+1
            k=k-1
        elif sum>tar:
            k=k-1
        else:
            j=j+1
        
print(result_sum)