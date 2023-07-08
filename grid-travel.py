def grid(n,m):
    if(n==0 or m==0):
        return 0
    if(m==1 and n==1):
        return 1
    else:
        return grid(m-1,n)+grid(m,n-1)
print(grid(2,3))
