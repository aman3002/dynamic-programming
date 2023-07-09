def bestsum(s,arr,memo={}):
    if(s in memo):
        return memo[s]
    if(s==0):
        return []
    if(s<0):
        return None
    l=None

    for i in arr:
        k=s-i
        p=bestsum(k,arr)
        if (p is not None):
            p.append(i)
            if(l is None or len(l)>len(p)):
                l=p.copy()
    memo[s]=l
    return memo[s]
print(bestsum(7,[5,2,3],{}))
print(bestsum(55,[5,7],{}))

