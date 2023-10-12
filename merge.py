def merge_list(list1, list2):
    # Check wheter  both inputs are lists or not
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Invalide input, please enter type List only")

    # Sort the value inside the list
    list1.sort()
    list2.sort()

    # Merge the sorted lists
    merged_list = []
    i = j = 0,0
    
    list1_size=len(list1)
    list2_size=len(list2)

    while i < list1_size and j < list2_size:
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append all the  remaining elements from both lists1 and list2
    while i < list1_size:
        merged_list.append(list1[i])
        i += 1
    while j < list2_size:
        merged_list.append(list2[j])
        j += 1
    return merged_list

