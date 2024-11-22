"""
1. Find the Target in a Sorted Array

Write a function binary_search(arr, target) that takes a sorted array arr and a target value target. It should return the index of target if it exists in the array, otherwise return None.
"""

def binary_search(arr, target):
    first = 0 
    last = len(arr) -1 

    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            first = mid + 1 
        else:
            last = mid - 1 
    return None

arr = [2, 3, 5, 8, 10, 14, 18]
target = 18 # Output: 6 (index of 18)
print("Target found at index: ", binary_search(arr, target))



"""
2. First Occurrence of a Target

In a sorted array, find the first occurrence of a given target. Return its index. If it doesn't exist, return None.
"""

def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid  # Store the index
            right = mid - 1  # Keep searching in the left half
        elif arr[mid] < target:
            left = mid + 1  # Move to the right half
        else:
            right = mid - 1  # Move to the left half

    return result

        
arr = [1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
target = 3 # Output: 5 (first index of 3)
print("First occurrence found at index: ", first_occurrence(arr, target))




"""
Find the Last Occurrence of an Element

Description: Given a sorted array, find the index of the last occurrence of a target element using binary search. If the target is not found, return None.

Input: [1, 2, 3, 3, 3, 4, 5, 7], target = 3
Output: 4 (index of the last occurrence of 3)
"""

def find_last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid  # Update the result to the current index
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

numbers = [1, 2, 3, 3, 3, 4, 5, 7]
target = 3
print("Last occurrence found at index: ", find_last_occurrence(numbers, target))
