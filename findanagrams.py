from collections import Counter
def find(s,p):
    s_len=len(s)
    p_len=len(p)
    p_count=Counter(p)
    s_count=Counter()
    result=[]
    for i in range(s_len):
        s_count[s[i]]+=1
        if i>=p_len:
            if(s_count[s[i-p_len]==1]):
                del(s_count[s[i-p-len]])
            else :
                s_count[s[i-p_len]]-=1
            if p_count==s_count:
                result.append(i-p_len+1)
    return result
print(find('abab','ab'))
