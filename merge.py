def merge_list(list1, list2):
    # Check if both inputs are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs should be lists")

    # Check if there are any non-integer elements in the input lists
    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("Input lists should only contain integers")

    # Merge the two lists
    merged_list = list1 + list2

    # Sort the merged list without using built-in sort functions
    sorted_list = merge_sort(merged_list)

    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append the remaining elements, if any
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# test
#if __name__ == "__main__":
   # list1 = [1, 5, 3, 7]
   # list2 = [6, 2, 4]
    #result = merge_list(list1, list2)
    #print(result)
