n=5
p=4
a=[]
summer=1+n//2
if(summer<p):pages=0
else :
 distance=summer-p
 left_distance=n-distance
 right_distance=distance-1
 if((n%2!=0 and p%2==0 ) and left_distance==1) : pages= 0
 elif((n%2!=0 and p%2==0) and right_distance==1): pages= 0
 elif(right_distance==1 or right_distance ==2):
        pages= 1
 elif(left_distance==1  or left_distance==2):
        pages= 1
 else :
        pages= distance//2
print (pages)

