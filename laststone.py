def lastStoneWeight(stones):

    import heapq
    heapq.heapify(stones)
    while stones:
     largest = (heapq.nlargest(2, stones))
     if(len(largest)==1):
      x=largest[0]
      break
      return stones[0]
     else:
      x = largest[0]
      y=largest[1]
     if(x==y):
       stones.remove(x)
       stones.remove(y)
     else :
        stones.remove(y)
        index_x=stones.index(x)
        stones[index_x]=x-y
    if(len(stones)==0):
     return 0
    else : return stones[0]






print(lastStoneWeight([2,2]))