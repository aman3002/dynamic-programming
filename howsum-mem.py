def howsum(s,arr,memo={}):
    if(s in memo):
        return memo[s]
    if(s==0):
        return []
    if(s<0):
        return None
    for i in arr:
        k=s-i
        p=howsum(k,arr)
        if (p is not None):
            p.append(i)
            memo[s]=p
            return memo[s]
print(howsum(7,[5,2,3]))
print(howsum(55,[5,7]))

