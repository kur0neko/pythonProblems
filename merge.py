def merge_list(list1, list2):
    i=0 
    j=0
    list1_size=len(list1)
    list2_size=len(list2)
    myList = []
    
    if (list1 != list and list2 != list):
        raise ValueError('Invalid input, the argument is not a list')
    
    else:
        while i< list1_size and j<list2_size:
            if list1[i] <= list2[j]:
                myList.append(list1[i])  
                i += 1
            else:
                myList.append(list2[j])
                j += 1
        myList.extend(list1[i:])  
        myList.extend(list2[j:]) 
        return myList
        
    
