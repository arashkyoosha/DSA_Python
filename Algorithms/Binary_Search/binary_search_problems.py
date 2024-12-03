"""

1. Find the Target (Easy)

Write a function to determine if a target value exists in a sorted array. Return True if the target exists and False otherwise.

Input: nums = [-10, -3, 0, 5, 9], target = 9
Output: True

"""

def find_target(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

nums = [-10, -3, 0, 5, 9]
target = -10
print("Target exists in the given array: ", find_target(nums, target))

nums = [-10, -3, 0, 5, 9]
target = 1
print("Target exists in the given array: ", find_target(nums, target))


"""

# 2. First Bad Version (Easy)

# Suppose you're an engineer working for a company that releases products in versions. You have an API isBadVersion(version) that returns whether a version is bad. Write a function to find the first bad version.

# Input: n = 5, where isBadVersion(4) and isBadVersion(5) return True.
# Output: 4

# """

# def isBadVersion(version):
#     left, right = 1, version
#     while left < right:
#         mid = left + (right - left) // 2
#         if isBadVersion(mid):
#             right = mid
#         else:
#             left = mid + 1
#     return left

# print(isBadVersion(5))

# def firstBadVersion(n: int) -> int:
#     left, right = 1, n  # Start with the full range of versions
    
#     while left < right:  # Keep narrowing the range
#         mid = left + (right - left) // 2  # Calculate the middle version
        
#         if isBadVersion(mid):  # If the mid version is bad
#             right = mid  # Move the right pointer to mid
#         else:  # If the mid version is good
#             left = mid + 1  # Move the left pointer to mid + 1
    
#     # When left == right, we've found the first bad version
#     return left

# print(firstBadVersion(5))


"""

3. Search Insert Position (Easy)

Given a sorted array of integers and a target value, return the index if the target is found. If not, return the index where it would be if inserted in order.

Input: nums = [1, 3, 5, 6], target = 5
Output: 2

"""

def find_index(arr, target):
    left = 0
    right = len(arr) -1 

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

nums = [1, 3, 5, 6, 6, 9, 99, 120, 1200, 5678, 104567]
target = 1200
print("Target found at index of: ", find_index(nums, target))


"""

4. Find Peak Element (Medium)

A peak element is an element that is strictly greater than its neighbors. Given a list of integers, find a peak element and return its index. You can assume the array will have at least one peak.

Input: nums = [1, 2, 3, 1]
Output: 2

"""

def find_peak(arr):
    left = 0
    right = len(arr) - 1   

    while left <= right:
        mid = (left + right) // 2

        # print(mid)
        # print(arr[mid])
        # print(mid - 1)
        # print(mid + 1)
        
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:          
            return mid             
        elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]: 
            left = mid + 1
        else:
            right = mid - 1        
    
nums = [1, 2, 3, 4, 5, 6, 5]
print("Peak element found at index: ", find_peak(nums))


"""
5. Find Minimum in Rotated Sorted Array (Medium)

Suppose an array of unique integers is sorted in ascending order and then rotated at an unknown pivot. Find the minimum element.

Input: nums = [4, 5, 6, 7, 0, 1, 2]
Output: 0

"""

def find_minimum(arr):
    left = 0
    right = len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:

    

nums = [4, 5, 6, 7, 0, 1, 2]    
find_minimum(nums)