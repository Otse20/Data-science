#Write a Python function all_true(1st) that takes a list of boolean values as input and returns True if all the values in the list are True, otherwise returns False. Use the built-in all() function to simplify your solution. Test it with different lists of boolean values.

def all_true(lst):
    return all(lst)

# Test cases
print(all_true([True, True, True]))  # True
print(all_true([True, False, True]))  # False
print(all_true([True, True, False]))  # False
print(all_true([True, True, True, True]))  # True
print(all_true([]))  # True (all() returns True for empty lists)


