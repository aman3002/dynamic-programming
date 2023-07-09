def howsum(s,arr):
    if(s==0):
        return []
    if(s<0):
        return None
    for i in arr:
        k=s-i
        p=howsum(k,arr)
        if (p is not None):
            p.append(i)
            return p
print(howsum(7,[5,2,3]))
print(howsum(55,[5,7]))
