def beyblade(n,g,o):
    testcase=0
    other = len(g) - 1
    while n==0:
     for i in range(len(g) - 1):
        if (g[i] > o[i]):
            testcase = testcase + 1
        else:
           while not(other <0) :
             if (o[i] < g[other]):
                temp = g[i]
                g[i] = g[other]
                g[other] = temp
                testcase=testcase+1
                break
             else:
                    other = other - 1
        other=len(g)-1
    print(g)
    print(o)
    print(testcase)

#beyblade(1,[3,6,7,5,3,5,6,2,9,1],[2,7,0,9,3,6,0,6,2,6])




def bey2():
    n = int(input())
    p = int(input())
    g = list(map(int, input().rstrip().split()))
    o = list(map(int, input().rstrip().split()))
    testcase = 0
    other = len(g) - 1
    for i in range(len(g) - 1):
        if (g[i] > o[i]):
            testcase = testcase + 1
        else:
            while not (other < 0):
                if (o[i] < g[other]):
                    temp = g[i]
                    g[i] = g[other]
                    g[other] = temp
                    testcase = testcase + 1
                    break
                else:
                    other = other - 1
        other = len(g) - 1
    print(testcase - 1)

bey2()