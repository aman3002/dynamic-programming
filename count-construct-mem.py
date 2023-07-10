def cont(s,arr,memo={}):
    if(s in memo):
        return memo[s]
    if(s==""):
        return 1
    else:
        t=0
        for i in arr:
            if(s.find(i)==0):
                k=s[len(i):]
                l=cont(k,arr)
                t=t+l
        memo[s]=t
        return memo[s]
print(cont(("abcd"),["abc","a","b","c"],{}))
print(cont("purple",["purp","p","ur","le","purpl"],{}))

