# Challenge 1: Basic Binary Search

def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

numbers = [1, 2, 4, 6, 8, 10, 12]
target = 6
print(binary_search(numbers, target))