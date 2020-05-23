def move(x):
    last_ind=0
    leg=len(x)-1
    count=0
    for i in range(len(x)):
        if(x[i]!=0):
                x[count]=x[i]
                count=count+1

    while count < len(x):
        x[count] = 0
        count += 1








    return x

res=move([1,0,3,0,12])
print(res)