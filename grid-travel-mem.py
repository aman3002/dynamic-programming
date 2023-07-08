def grid(m,n,memo):
    if(m==0 or n==0):
        return 0
    if(m==1 and n==1):
        return 1
    else:
        if((m,n) in memo):
            return memo[(m,n)]
        memo[(m,n)]=grid(m-1,n,memo)+grid(m,n-1,memo)
        return memo[(m,n)]
print(grid(2,3,{}))

