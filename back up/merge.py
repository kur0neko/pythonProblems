def merge_list(list1, list2):
    i,j=0,0
    
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Invalide input, please enter type List only")
    
    list1_size=len(list1)
    list2_size=len(list2)
    myList = []
    
    while i< list1_size and j< list2_size:
        if list1[i] <= list2[j]:
            myList.append(list1[i])  
            i += 1
        else:
            myList.append(list2)
            j += 1
        myList.extend(list1[i:])  
        myList.extend(list2[j:]) 
        return myList
