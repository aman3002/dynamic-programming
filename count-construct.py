def cont(s,arr):
    if(s==""):
        return 1
    else:
        t=0
        for i in arr:
            if(s.find(i)==0):
                k=s[len(i):]
                l=cont(k,arr)
                t=t+l
        return t
print(cont(("abcd"),["abc","a","b","c"]))
print(cont("purple",["purp","p","ur","le","purpl"]))
