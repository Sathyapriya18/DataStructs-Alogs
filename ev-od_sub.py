def isHappy(x):
    digi=digits(x)
    mutliplier=10
    a=x//mutliplier

    b = x % 10
    c=(a*a)+(b*b)

    if(c==1):
        return 'true'
    else : isHappy(c)
    return 'false'

def digits(x):
    digi=0
    while x>0:
        digi=digi+1
        x=x//10
    return digi


def maxSubArray( nums):
    import sys
    INT_MIN = -sys.maxsize-1
    sumtil = 0
    maxsum = INT_MIN
    if(len(nums)==1): maxsum=nums[0]
    else :
     for i in range(len(nums)):
         sumtil=nums[i] + sumtil

         if (sumtil > maxsum):
            maxsum = sumtil
    return maxsum

#res=maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#print('this res',res)
isHappy(19)
