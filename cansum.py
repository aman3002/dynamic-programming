def cansum(s,arr):
    if(s==0):
        return True
    if(s<0):
        return False
    for i in arr:
        k=s-i
        if(cansum(k,arr)==True):
            return True
print(cansum(7,[5,2,3]))
