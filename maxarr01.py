def findSubArray(arr, n):
    sum = 0
    maxsize = 0
    startindex=-1
    # Pick a starting point as i

    for i in range(0, n - 1):

        sum = -1 if (arr[i] == 0) else 1

        # Consider all subarrays starting from i

        for j in range(i + 1, n):

            sum = sum + (-1) if (arr[j] == 0) else sum + 1

            # If this is a 0 sum subarray, then
            # compare it with maximum size subarray
            # calculated so far

            if (sum == 0 and maxsize < j - i + 1):
                maxsize = j - i + 1
                startindex = i

    if (maxsize == -1):
               print("No such subarray");
    else:
        print(startindex, "to", startindex + maxsize - 1);

    return maxsize


arr = [[1,1,1,1,1,1,1,1]]
size = len(arr)
print(findSubArray(arr, size))