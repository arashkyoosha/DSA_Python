"""

Problem 1: Find a Number in a List

Write a function that takes a list of integers and a target number as input. Use linear search to determine if the target number exists in the list. Return the index of the target if found; otherwise, return None.

"""

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


"""

Problem 2: Count Occurrences

Given a list of integers, write a function to count how many times a specific number occurs in the list.


"""

def count_nums(list, target):
    indices = []
    for i in range(0, len(list)):
        if list[i] == target:
            indices.append(i)
    return indices

numbers = [1,2,3,2,5,7,2]
target = 2
print(count_nums(numbers, target))


"""

Problem 3: Find Maximum

Write a function that takes a list of integers and returns the largest number in the list using linear search.

"""

def find_largest(list):    
    largest = 0
    for i in range(largest, len(list)): 
        if largest < list[i]:
            largest = list[i]
    return largest   

numbers = [1,3,6,8,77,4,66,23,12,120,55,14]
print(find_largest(numbers))


"""

Problem 4: Find Minimum in a Range

Write a function that takes a list of integers and two indices (start and end) as input. Use linear search to find and return the smallest number in the sub-list between these indices (inclusive).

"""

def find_min_range(list, startIndex, endIndex):
    smallest = list[startIndex]
    for i in range(startIndex, endIndex):
        if smallest > list[i]:
            smallest = list[i]
    return smallest       
    

numbers = [1,3,6,8,77,4,66,23,12,120,55,14]
print(find_min_range(numbers, startIndex=6, endIndex=10))



"""

Problem 5: Multiple Matches

Given a list of integers, write a function to return a list of all indices where a specified number occurs. If the number doesn't appear, return an empty list.

"""