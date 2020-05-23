def compareTriplets(a, b):
    res=[]
    m=0
    n=0
    for i in range(len(a)):
        if(a[i]>b[i]):
            m=m+1
        elif(a[i]<b[i]):
            n=n+1
        elif(a[i]==b[i]):
            continue
    res.append(m)
    res.append(n)
    return res

def verybig(arr):
    ar_count=len(arr)
    count = 0
    for i in range(ar_count):
        count = count + arr[i]
    return count

result=verybig([1000000001, 1000000002 ,1000000003, 1000000004, 1000000005])
print (result)