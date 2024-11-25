def binary_search(lst, target):
    first = 0 
    last = len(lst) -1 

    while first <= last:
        midpoint = (first + last) // 2 

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1 
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10] # IT HAS TO BE SORTED IN ASCENDING ORDER

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

result = binary_search(numbers, 10)
verify(result)



# def find_index(arr, target):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1 
#         else:
#             right = mid - 1

#     return None

# nums = [1,3,5,7,8,15,55,87,120,137]
# target = 137
# print("Target found at index: ", find_index(nums, target))