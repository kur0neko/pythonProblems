def merge_list(list1, list2):
    i,j=0,0
    
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Invalide input, please enter type List only")
    

    
    list1_size=len(list1)
    list2_size=len(list2)
    
    sort_List1=[]
    sort_List2=[]
    for i in range(list1_size):
            sort_List1.append(sorted(list1, key= lambda x:x[i]))
        
    for i in range(list2_size):
            sort_List2.append(sorted(list2, key= lambda x:x[i]))    
    
  
    myList = []
    
    while i< len(sort_List1) and j< len(sort_List2):
        if sort_List1[i] <= sort_List1[j]:
            myList.append(sort_List1[i])  
            i += 1
        else:
            myList.append(sort_List2)
            j += 1
        myList.extend(sort_List1[i:])  
        myList.extend(sort_List2[j:]) 
        return myList
