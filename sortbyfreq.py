from collections import Counter

def sortfreq(s):
    result=''
    scount={}

    for i in s:
        if i in scount:
            scount[i]+=1
        else  :
            scount[i]=1

    schar=sorted(scount,key=lambda x:scount[x],reverse=True)
    for char in schar :
        result+=char*scount[char]
    print(result)

sortfreq('tree')