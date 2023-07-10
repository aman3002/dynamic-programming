def can(s,arr,memo={}):
    if(s in memo):
        return memo[s]
    if(s==""):
        return True
    else:
        for i in arr:
            if( s.find(i)==0):
                k=s[len(i):]
                if(can(k,arr)==True):
                    memo[s]=True
                    return memo[s]
        return False
print(can(("abcd"),["a","b","c","d"],{}))
