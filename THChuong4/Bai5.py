def fib(n):
    if n<=2:
        return 1
    return (fib(n-1)+fib(n-2))

def listFib(n):
    for i in range(1,n+1):
        print(fib(i),end="\t")
        
print(fib(9))

listFib(9)