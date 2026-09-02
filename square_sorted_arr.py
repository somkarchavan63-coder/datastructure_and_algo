import numpy as np
#condition the array consist of negative numbers also

arr=np.array([-4,-1,0,1,2,4])
final_array=np.array([])
arr1=np.array([])
arr2=np.array([])
arr_len=len(arr)
i=0
while i<=arr_len-1:
    if arr[i]<0:
        arr1=np.append(arr1,arr[i])
        i=i+1
    else:
        arr2=np.append(arr2,arr[i])
        i=i+1
print(arr1)
print(arr2)

def square_arr(arr):
    arr_len=len(arr)
    i=0
    while i<=arr_len-1:
        squr=arr[i]*arr[i]
        arr[i]=squr
        i=i+1
    return arr

a1=square_arr(arr1)
print(a1)
a2=square_arr(arr2)
print(a2)

i=len(arr1)-1
j=0
while i>=0 and j<=len(arr2)-1:
    if arr1[i]==arr2[j]:
        final_array=np.append(final_array,arr1[i])
        final_array=np.append(final_array,arr2[j])
        i=i-1
        j=j+1
    elif arr1[i]>arr2[j]:
        final_array=np.append(final_array,arr2[j])
        j=j+1
    else:
        final_array=np.append(final_array,arr1[i])
        i=i+1

print(final_array)