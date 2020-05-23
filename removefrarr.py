def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i]=nums[j]
            nums[j] = nums[i]
            j = j + 1

    return j


res=removeElement([3,3,2,2,3],3)
print(res)