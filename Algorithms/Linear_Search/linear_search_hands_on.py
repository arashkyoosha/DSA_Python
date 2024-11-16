# Problem 1: Find a Number in a List

"""Write a function that takes a list of integers and a target number as input. Use linear search to determine if the target number exists in the list. Return the index of the target if found; otherwise, return None."""

def find_value(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = find_value(numbers, 6)
verify(result)

result = find_value(numbers, 15)
verify(result)