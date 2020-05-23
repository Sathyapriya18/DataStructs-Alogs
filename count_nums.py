def countElements(arr) :
    counter = 0
    i=0
    other = len(arr) - 1
    while(i<len(arr)):

         if(other==i):
            other=other-1
         if (arr[other] == arr[i] + 1 and not(other<0)):
            counter = counter + 1
            i=i+1
            other=len(arr)-1
         else :
          other=other-1
          if(other<0):
              other=len(arr)-1
              i=i+1

    print( counter)


countElements([1,3,2,3,5,0])