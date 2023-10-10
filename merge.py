def merge(list1, list2):
    i=0 
    j=0
    mergeList = []
    while i<len(list1) and j<len(list2):
        if list1[i] <= list2[j]:
            mergeList.append(list1[i])  
            i += 1
            
        else:
            mergeList.append(list2[j])
            j += 1
    mergeList.extend(list1[i:])  
    mergeList.extend(list2[j:]) 
    return mergeList