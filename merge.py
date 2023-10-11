def merge_list(list1, list2):
    i,j=0,0
    myList = []
    
    while i< len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            myList.append(list1[i])  
            i += 1
        else:
            myList.append(list2[j])
            j += 1
    myList=myList+list1[i:]+list2[J:]
    return myList
    
        #raise ValueError('invalid input')