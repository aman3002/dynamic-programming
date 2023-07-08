def fib(n,memo):
    if(n in memo):
        return memo[n]
    else:
    
        if(n<=2):
            return 1
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        print(memo)
        return memo[n]

n=7
print(fib(n,{}))
