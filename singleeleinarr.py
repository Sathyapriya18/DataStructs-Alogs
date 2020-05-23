from collections import Counter

def singleelem(s):
    p=Counter(s)
    for ele in p.items() :
        if(ele[1]==1):
            return ele[0]

print(singleelem([3,3,7,7,10,11,11]))

