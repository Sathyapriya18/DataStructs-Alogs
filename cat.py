def cat(x,y,z) :
    result=''
    for i in range(1, x):
        for a in [y, z]:
            dist1 = a[1] - a[0]
            dist2 = a[2] - a[1]
            if (dist1 == dist2):
                result = result + " "+ 'Mouse C' + "\n"
            elif (dist1 > dist2):
                result = result + " "+'Cat B' + "\n"
            else:
                result = result +" "+ 'Cat A' + "\n"
    return (result)


res=cat(2,[1,2,3],[1,3,2])
print(res)
