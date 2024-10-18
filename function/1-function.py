# Write a Python function that takes a string and two indices, start and end, and 
# returns a new string that consists of every second character between the start and end indices (inclusive). 
# For example, for the input string "abcdefghijklmnopqrstuvwxyz" and indices 4 and 40, 
# the output should be "egikmoq". Handle cases where the start or end indices are out of range.

def slicing_string(s, start, end):

    if start < 0:
        start = 0

    if end >= len(s):
        end = len(s) - 1
        
    return s[start:end+1:2]

input_string = "abcdefghijklmnopqrstuvwxyz"
start_indices = 4
end_indices = 20
result = slicing_string(input_string, start_indices, end_indices)
print(f"The result is {result}")

