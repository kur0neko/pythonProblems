def merge_list(list1, list2):
    i=0 
    j=0
    myList = []
    while i< len(list1) and j<len(list2):
        if list1[i] <= list2[j]:
            myList.append(list1[i])  
            i += 1
            
        else:
            myList.append(list2[j])
            j += 1
    myList.extend(list1[i:])  
    myList.extend(list2[j:]) 
    return myList