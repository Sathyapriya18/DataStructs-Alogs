def reverse(x):
    rev = 0
    while(x>0):

     rem=(x%10)
     rev = rev * 10 + rem
     x = x // 10
    print(rev)


#reverse(123)

def negrev(x):
    x = str(x)
    if x[0] == '-':
        a = int('-' + x[-1:0:-1])
        if a >= -2147483648 and a <= 2147483647:
            return a
        else:
            return 0
    else:
        a = int(x[::-1])
        if a >= -2147483648 and a <= 2147483647:
            return a
        else:
            return 0
res=negrev(123)
print(res)

