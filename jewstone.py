def js(S,J):
    count=0
    for s in S:
        for j in J:
            if(s==j):
             count+=1
    return count

print(js('aaAA','ab'))