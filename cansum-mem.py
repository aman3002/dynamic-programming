def cansum(s,arr,memo={}):
    if(s in memo):
        return memo[s]
    if(s==0):
        return True
    if(s<0):
        return False
    for i in arr:
        k=s-i
        if(cansum(k,arr)==True):
            memo[s]=True
            return memo[s]
print(cansum(7,[5,2,3]))

