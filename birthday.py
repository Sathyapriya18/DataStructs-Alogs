def candle(arr):
    arr.sort()
    c=max(arr)
    count=0
    for i in range(len(arr)):
        if(arr[i]==c):
            count=count+1
    print (count)
   
candle([3,2,3,1])