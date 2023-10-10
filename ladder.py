def my_steps(n):
    if n<1 or n > 25:
            raise ValueError('n is out of boudary')
    if n==1 or n==2:
        return n
    else:
        return my_steps(n-1)+my_steps(n-2)
    
    
    


        
        


    


    