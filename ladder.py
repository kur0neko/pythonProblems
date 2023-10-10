def my_steps(n):
    if n<1 or n > 25:
        try:
            raise ValueError('n is out of boudary')
        except ValueError as e:
            print(str(e))
    if n==1:
       return n
    elif n==2:
        return n
    else:
        return my_steps(n-1)+my_steps(n-2)
    
    
    


        
        


    


    