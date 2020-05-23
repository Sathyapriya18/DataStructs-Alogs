def diag(arr):
    n = 3
    firs_sum=0
    second_sum=0
    for i in range(n):
        first_diag=firs_sum+arr[i][i]
        firs_sum=first_diag
    for m in range(n):
         j=n-1-m
         print(m,j)
         second_diag=second_sum+arr[m][j]
         second_sum=second_diag
    return abs(first_diag - second_diag)



res=diag([[1,2,3],[4,5,6],[7,8,9]])
print (res)
