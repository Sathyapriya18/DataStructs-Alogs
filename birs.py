def bird(arr) :
 arr_count=len(arr)
 count=0
 ctr=0
 bird_list=[]
 arr.sort()
 for i in range(0,arr_count):
     for j in range(1,arr_count):
          if(arr[i]==arr[j]):
            count=count+1
     if(count>ctr):
      ctr=count
      bird_list.append(arr[i])
     count=0
 print( bird_list[len(bird_list)-1])


def birds(arr):
 types = arr
 counts=[0]*5
 for i in range(len(arr)):
    counts[types[i]-1]+=1
 m=0
 mi=-1
 for i in range(5):
    if counts[i]>m:
        m=counts[i]
        mi=i
 print (mi+1)
 return mi+1




birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])