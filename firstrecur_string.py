def firstrecurstring(x):

    j=len(x)-1
    for i in range(len(x)):
        if(x[i]==x[j]):
            return x[i]
        else : j=j-1



res=firstrecurstring('DBCABA')
print(res)