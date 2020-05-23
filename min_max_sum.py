def min_max(arr):
 min_sum = 0
 max_sum = 0
 mid = len(arr) // 2
 print(mid)
 i=0
 j=mid-1
 res=[]
 for _ in range(0, mid):
     min_sum = min_sum + arr[i] + arr[i + 1]
     i=i+2
 res.append(min_sum)

 for _ in range(mid):
    max_sum = max_sum + arr[j] + arr[j + 1]
    j=j+2
 res.append(max_sum)

 return min


res=min_max([1,2,3,4,5])
print (res)