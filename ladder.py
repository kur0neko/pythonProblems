def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
    
def my_steps(n):
    if n<1 or n >25:
        try:
            raise ValueError('n is out of boudary')
        except ValueError as e:
            print(str(e))
    else:
        return fib(n+1)


        
        


    


    