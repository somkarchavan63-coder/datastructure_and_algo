import numpy as np
"""arr=np.array([-1,0,1])
i=0
j=1
k=len(arr)-1
arr_len=len(arr)
result=[]
for i in range(len(arr)-2):
  if i>0 and arr[i]==arr[i-1]:
     continue
  j=i+1
  k=arr_len-1
  tar=-(arr[i])
  while j<k:
    sum=-1*arr[i]
    s=arr[j]+arr[k]
    if s==sum:
        result.append([int(arr[i]),int(arr[j]),int(arr[k])])
        j=j+1
        k=k-1
        while j<arr_len-1 and arr[j]==arr[j-1]:
            j=j+1
        while k>=0 and arr[k]==arr[k+1]:
            k=k-1
    elif s<sum:
        j=j+1
    else:
        k=k-1

print(result)"""
""" sorting"""
"""arr1=np.array([2,5,1,3,6,7])
i=0
j=len(arr1)-1
while i<len(arr1)-1:
     if arr1[i]<arr1[j]:"""

class triplet_sum_zero:
    def __init__(self,arr,tar):
        self.arr=arr
        self.tar=tar

    def find_triplet(self):
        result=[]
        arr_len=len(self.arr)
        for i in range(arr_len-2):
            j=i+1
            k=arr_len-1
            sum=-(self.arr[i])
            while j<k:
                s=self.arr[j]+self.arr[k]
                if s==sum:
                    result.append([int(self.arr[i]),int(self.arr[j]),int(self.arr[k])])
                    j=j+1
                    k=k-1
                    while j<arr_len and self.arr[j]==self.arr[j-1]:
                        j=j+1
                    while k>=0 and self.arr[k]==self.arr[k+1]:
                        k=k-1
                elif s<sum:
                    j=j+1
                else:
                    k=k-1
        return result

obj=triplet_sum_zero(np.array([-1,0,1]),0)
print(obj.find_triplet())





  

