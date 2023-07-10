def can(s,arr):
    if(s==""):
        return True
    else:
        for i in arr:
            if( s.find(i)==0):
                k=s[len(i):]
                if(can(k,arr)==True):
                    return True
        return False
print(can(("abcd"),["a","b","c","d"]))
