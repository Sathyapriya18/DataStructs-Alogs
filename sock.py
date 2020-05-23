a=[2,1,3,5,3,2]
indi=[]
for i in range(len(a)):
    for j in range(len(a)):
        j=j+1
        if(j==len(a) or j==i): break
        else:
            if(a[i]==a[j]):
                indi.append(j)
for m in range(len(indi)):
    if(indi[m]>indi[m+1] and m+1 >= len(indi)):
        mini=indi[m+1]
print (mini)
