# Challenge 1: Basic Linear Search

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1 

numbers_1 = [1, 2, 3, 4, 5]
target = 3
numbers_2 = [10, 20, 30, 40, 50]
target_2 = 25
print("Found at index: ", linear_search(numbers_1, target))  # Output: 2
print(linear_search(numbers_2, target_2))  # Output: -1



# Challenge 2: Linear Search with Multiple Occurrences


def linear_search_multiple(lst, target):
    # return [i for i, value in enumerate(lst) if value == target]     # << Fast and easy in one line
    
    indices = []
    for i in range(0, len(lst)):
        if lst[i] == target:
            indices.append(i)
    return indices
            
            
numbers_a = [1, 2, 3, 2, 4, 2]
target_a = 2
print(linear_search_multiple(numbers_a, target_a))  # Output: [1, 3, 5]

numbers_b = [5, 6, 7, 8, 5]
target_b = 10
print(linear_search_multiple(numbers_b, target_b))  # Output: []


# Problem 3: Find Maximum Element's Index

def find_max_index(arr):
    max_value = 0
    for i in range(0, len(arr)):
        if arr[i] > max_value:
            index = i
            max_value = arr[i]
    return index, max_value
    
            
arr = [5, 9, 2, 20, 15, 43, 6] # Output should be 5 - index of 43
print(find_max_index(arr))



# Problem 4: Check if the Array is Sorted

def is_sroted(arr):
    for i in range(0, len(arr)):
        starting_value = arr[0]
        if starting_value > arr[i]:
            return False
    return True


arr1 = [1, 2, 3, 4, 5] # Output: True

arr2 = [5, 3, 2, 1] # Output: False

arr3 = [5, 6, 7, 8, 0] # Output: False

print(is_sroted(arr3))


# Problem 5: Find the First Negative Number

def find_first_negative(arr):
    for i in range(0, len(arr)):
        if arr[i] < 0:
            return i
    return -1

arr = [3, 7, -8, 0, -2, 4, -5] # Output: 2 - Index of -8
print(find_first_negative(arr))
