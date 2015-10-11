def fib_loop(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
    fib = [1,1]
    
    for i in range(n-2)
        x= fib[i]+fib[i-1]
        fib.append(x)
        
    return fib[n-1]
    
def fib_recursion(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
    fib1=1
    fib2=1
    
    for i in range(n-2):
        fib3 = fib2 + fib1
        fib1 = fib2
        fib2 = fib3
        
    return fib3

print(fib_loop(8))
print(fib_recursion(13))
