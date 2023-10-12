def merge_list(list1, list2):
    i,j=0,0
    
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Invalide input, please enter type List only")
    
    #list1.sort()
    #list2.sort()

    list1_size=len(list1)
    list2_size=len(list2)
    
    sorted_List1=[i for i, x in sorted(enumerate(list1), key=lambda x: x[1])]
    sorted_list2=[i for i, x in sorted(enumerate(list2), key=lambda x: x[1])]
    myList = []
    
    while i< list1_size and j<list2_size:
        if sorted_List1[i] <= sorted_List2[j]:
            myList.append(sorted_List1[i])  
            i += 1
        else:
            myList.append(sorted_List2[j])
            j += 1
        myList.extend(sorted_List1[i:])  
        myList.extend(sorted_List2[j:]) 
        return myList
