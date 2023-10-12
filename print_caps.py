def allcaps(fun):
    
    def wrapper():

        res = fun()
        modified = res.upper()
        return modified
    return wrapper
