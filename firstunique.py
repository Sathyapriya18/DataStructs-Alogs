import collections
def firstUniqChar( s: str) -> int:
    count = collections.Counter(s)

    # find the index
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


print(firstUniqChar('leetcode'))