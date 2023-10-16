"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of O(log N), where N is the length of the list.
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element.
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

State the problem.

Given a sorted list that was rotated, find out the number of times it was rotated.
Basically, rotating the list means that an element has shifted from 0 to a new position.


nums: array of numbers

rotations: our output, equal to the number of the steps an element has shifted.

We can find out if there has been a rotation from the previous element being larger than an observed element.
"""

tests = [
    {"input": {"nums": [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, "output": 3},
    {"input": {"nums": [7, 9, 11, 14, 39, 1, 3, 6, ]}, "output": 5},
    {"input": {"nums": [1, 5, 10]}, "output": 0},
    {"input": {"nums": [14, 1, 3, 6, 7, 9, 11]}, "output": 1},
    {"input": {"nums": [2, 6, 8, 9, 12, 14, 1]}, "output": 6},
    {"input": {"nums": []}, "output": 0},
    {"input": {"nums": [2]}, "output": 0},
]


# Let's pretend to do linear
def count_rotations_linear(nums):
    count = 1
    while count < len(nums):
        if nums[count] < nums[count-1]:
            return count
        else:
            count += 1
    return 0


# for test in tests:
#     answer = count_rotations_linear(test['input']['nums'])
#     print(f"Looking at {test['input']['nums']}. Expecting {test['output']}. Got {answer}.")

# This has a O(n) time complexity, O(1) space complexity


# Let's do binary search style
def count_rotations_binary(nums):
    first = 0
    last = len(nums)-1
    while first <= last and len(nums) > 0:
        midpoint = (first + last)//2
        if midpoint > 0 and nums[midpoint] < nums[midpoint-1]:
            return midpoint
        elif nums[last] > nums[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return 0

for test in tests:
    answer = count_rotations_binary(test['input']['nums'])
    print(f"Looking at {test['input']['nums']}. Expecting {test['output']}. Got {answer}.")

# Time complexity O(log N), space complexity O(1)

bonus_tests = [
    {"input": {"nums": [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]}, "output": 6},
    {"input": {"nums": [3, 4, 4, 5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3]}, "output": 9},
    {"input": {"nums": [0, 0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9, 9]}, "output": 0},
    {"input": {"nums": [9, 0, 0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9]}, "output": 1},
    {"input": {"nums": [0, 2, 3, 3, 3, 3, 4, 4, 5, 6, 6, 9, 9, 9, 0]}, "output": 14},
    {"input": {"nums": []}, "output": 0},
    {"input": {"nums": [2]}, "output": 0},
]

for test in bonus_tests:
    answer = count_rotations_binary(test['input']['nums'])
    print(f"Looking at {test['input']['nums']}. Expecting {test['output']}. Got {answer}.")