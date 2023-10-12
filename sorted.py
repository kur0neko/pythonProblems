def reverse_sort_dictionary(input_dict):
  
    sorted_items = sorted(input_dict.items(), key=lambda x: x[0], reverse=True)
    
    result = [(name, data[0]) for name, data in sorted_items]
    
    return result

