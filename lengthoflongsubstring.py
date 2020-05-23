def lengthOfLongestSubstring(s: str) -> int:
    sub_s = ""
    len_sub = 0
    for j in s:
        if j not in sub_s:
            sub_s += j
        else:
            len_sub = max(len_sub, len(sub_s))
            sub_s = sub_s[(sub_s.index(j) + 1)::] + j

    len_sub = max(len_sub, len(sub_s))
    return len_sub

res=lengthOfLongestSubstring('abcabcab')
print(res)

