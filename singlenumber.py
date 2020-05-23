from collections import Counter
def single(nums):
    count = Counter(nums)
    for _ in count:
        least = min(count.keys())
    for j in (count.items()):
        print(j)






res=single([1,2,2,4,1])
print(res)