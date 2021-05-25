def fib(n):
    a,b = 0,1
    for x in range(n-1):
        a, b = b, a + b
    return a 

#print(fib(10))

def fibr(n):
    if n <= 1:
        return n
    else:
        return fibr(n-1) + fibr(n-2)
    
print(fibr(5))
     




