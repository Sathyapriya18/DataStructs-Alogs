def subarraySum( nums, k: int) -> int:
    sumdict = {0: 1}
    count = 0
    s = 0
    for num in nums:
        s += num
        if (s - k) in sumdict:
            count +=1
        if s in sumdict:
            sumdict[s] += 1
        else:
            sumdict[s] = 1
    return count

print(subarraySum([3,4,7,2,-3,1,4,2],7))