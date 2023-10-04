"""
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""

"""
1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"""

"""
1. State the problem. Identify the input & output formats.
"""

"""
Problem: Write a program that finds a position of a given number in a list of numbers arranged in decreasing order.
We need to minimise the number of times we access elements from the list.

Inputs: 
- cards (a list)
- query (given number)

Output:
- Position


Cases:
The number query occurs somewhere in the middle of the list cards.
query is the first element in cards.
query is the last element in cards.
The list cards contains just one element, which is query.
The list cards does not contain number query.
The list cards is empty.
The list cards contains repeating numbers.
The number query occurs at more than one position in cards.

"""

"""
3: Solution.
With linear search:
Look at the first element
If it is a match, return its position in the list
If not a match, go to the next element, increasing the position by one
Keep going until there is a match or you reach the end of the list.
If number not found, return -1

"""

tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}]


def linear_search_card(cards, query):
    position = 0
    while position <= len(cards) - 1:
        if query == cards[position]:
            return position
        else:
            position += 1
    return -1


# print("Linear search")
# for case in tests:
#     print(f"Doing a test, trying to find {case['input']['query']} in {case['input']['cards']}")
#     answer = linear_search_card(case["input"]["cards"], case["input"]["query"])
#     print(f"Expecting {case['output']}, got {answer}")
# print("____________")

"""
Analysing algorithm's complexity
Time: O(n)
Space: O(1)
"""

"""
We can improve this by applying a binary search.

Wtih binary search:

Find the middle (floor) position of the list
Compare element at middle position with the answer
If the element at the middle position is correct, return that position
If the element is too big, that means that the answer is to the right, so keep that half of the list
If the element is too small, that means that the answer is to the left
Find the middle position of the new list and repeat
If you end up with a list with one or 0 elements and you still haven't found it, return a -1

"""

"""
List has 4 elements : 0, 1, 2, 3
List of 5 elements: 0, 1, 2, 3, 4
"""


def binary_search_card(cards, query):
    first = 0
    last = len(cards)-1
    while first <= last:
        midpoint = (last+first)//2
        # print(f"First is {first}, Last is {last}")
        # print(f"midpoint is {midpoint}")
        # print(f"Array is {cards[first:last]}")
        if cards[midpoint] == query:
            if cards[midpoint - 1] == query and midpoint !=0:
                last = midpoint - 1
            else:
                return midpoint
        elif cards[midpoint] > query:
            first = midpoint+1
        else:
            last = midpoint-1
    return -1


for case in tests:
    print(f"Doing a test, trying to find {case['input']['query']} in {case['input']['cards']}")
    answer = binary_search_card(case["input"]["cards"], case["input"]["query"])
    print(f"Expecting {case['output']}, got {answer}")
print("____________")
