#Write a Python program to remove duplicates from a list. For example, given the list [1, 2, 2, 3, 4, 4, 5], the output should be [1, 2, 3, 4, 5].

def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)
