#Write a Python function that concatenates two lists list1 and list2, then removes all duplicate elements from the concatenated list and returns the resulting list. Test the function with two lists containing both common and unique elements

def concat_remove_duplicates(list1, list2):
    # Concatenate lists
    concatenated_list = list1 + list2
    
    # Remove duplicates using set
    unique_list = list(set(concatenated_list))
    
    return unique_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = concat_remove_duplicates(list1, list2)
print(result)
