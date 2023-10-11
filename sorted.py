def sort_dictionary(adict):
    sorted_keys = sorted(adict.keys(), key = lambda x: adict[x][1])
    
    result = []
    for k in sorted_keys:
        
        atuple = (k,adict[k][0])
        result.append(atuple)
        
    return result