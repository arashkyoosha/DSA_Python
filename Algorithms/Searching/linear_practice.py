
# def find_letters(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             arr.append(arr[i])
#             print("Letters found at index: ", i)
#     return -1

# letters = ["A", "B", "C", "O", "D", "C", "E", "F", "G", "C", "H", "I"]
# target = "C"
# find_letters(letters, target)



def linear_search(arr, target): # Challenge 1: Basic Linear Search
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1
    
    
def find_indices(lst, value): # Challenge 2: Linear Search for Multiple Occurrences
    return [i for i, x in enumerate(lst) if x == value]
    
def linear_early(lst, target): # Challenge 3: Linear Search with Early Exit
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
            break
    return -1
    
def linear_string(str, char): # Challenge 4: Linear Search in a String
    for s in range(0, len(str)):
        if str[s] == char:
            return s
    return -1
    
def linear_multiple_strings(string, char): #Linear Search for Multiple Occurrences
    return [s for s, x in enumerate(string) if x == char]

def linear_string_case_insensitive(str, char): # Challenge 5: Case-Insensitive Linear Search   
    for s in range(0, len(str)):
        lower_char = str[s].lower()
        if lower_char == char:
            return s
    return -1

def linear_search_in_matrix(matrix, target): # Challenge 6: Linear Search in a Matrix
    for i in range(0, len(matrix)):
        if matrix[i][i] == target:
            return i, i
    return (-1, -1)


""" Functions above """


arr = [10, 23, 45, 70, 11, 15]
target = 70
print("Found at index: ", linear_search(arr, target))  # Output should be 3


my_list = [10, 23, 45, 70, 11, 15, 45, 56, 99, 70, 45, 33, 87]
target = 45
print("Found at index: ", find_indices(my_list, target)) # Output should be 2, 4, 10


numbers = [10, 23, 47, 70, 11, 15, 43, 56, 99, 70, 44, 33, 87]
target_num = 43
print("Found at index: ", linear_early(numbers, target_num)) # Output should be 6


s = "hello world"
char = "o"
print("Found at index: ", linear_string(s, char))  # Output should be 4


s = "hello world"
char = "o"
print("Found at index: ", linear_multiple_strings(s, char))  # Output should be 4 and 7


s = "Hello World"
char = "h"
print("Found at index: ", linear_string_case_insensitive(s, char))  # Output should be 0
  
       
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
target = 50
print("Found at: ", linear_search_in_matrix(matrix, target))  # Output should be (1, 1)

