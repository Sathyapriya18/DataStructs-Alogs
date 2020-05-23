def powerpuff(n,li,qu):
    count=[]
    for i in range(len(li)):
        count.append(qu[i]/li[i])
    count.sort()
    print(count[0])



powerpuff(4,[2,5,6,3],[20,40,90,50])