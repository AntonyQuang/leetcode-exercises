"""
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.

1: State the problem clearly. Identify the input & output formats.
2: Come up with some example inputs & outputs. Try to cover all edge cases.
3: Come up with a correct solution for the problem. State it in plain English.
4: Implement the solution and test it using example inputs. Fix bugs, if any.
5: Analyze the algorithm's complexity and identify inefficiencies, if any.
6: Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

1. Stating the problem, input and output.

Problem:
Write a program to find the position of a given number in a list of numbers arranged in decreasing order.
We also need to minise the number of times we access elements from the list.

Input:
1. cards: list of numbers sorted in decreasing order
2. query: number, whose position in the array is to be determined

Output:
3. position: postion of query in the list of cards
"""

tests = [{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
         {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
         {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
         {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
         {'input': {'cards': [6], 'query': 6}, 'output': 0},
         {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
         {'input': {'cards': [], 'query': 7}, 'output': -1},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
          'output': 7},
         {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
           'query': 6},
          'output': 2}]

"""
Linear Search Based Solution:
1. Start with a position of 0.
2. Compare the element in that position with the query, if it matches, return the position.
3. If not, add 1 to the position.
4. Repeat steps 2-3 until you reach the end of the list
5. Return -1 if nothing is found
"""


# Linear search time
def linear_search(cards, query):
    position = 0
    while position <= len(cards)-1:
        if cards[position] == query:
            return position
        else:
            position += 1
    return -1


# for case in tests:
#     answer = linear_search(case["input"]["cards"], case["input"]["query"])
#     print(f"Looking for {case['input']['query']} in {case['input']['cards']}")
#     print(f"Expecting {case['output']}, got {answer}")

"""
Time complexity: O(n)
Space complexity: O(1)
"""

"""
Binary Search based solution
1. Establish your first and last points of the range you want to look at.
2. Make a midpoint based on that
3. Find element at the midpoint
4. If element is the same as the query, return the mid point
5. If the element is smaller than the query, then the query is to the left of the element. Look at only the left side by
making a value of "last" the position before the midpoint
6. If the element is larger than the query, then the query is to the right of the element. Look at only the right side by
making a value of "first" the position after the midpoint
7. Repeat steps 1-6
7. If "first" and "last" meet up, that is the last iteration, and if it doesn't find it then, return -1
"""


def binary_search(cards, query):
    first = 0
    last = len(cards)
    while first <= last and len(cards)>0:
        midpoint = (first + last) // 2
        if cards[midpoint] == query:
            if cards[midpoint-1] == query and midpoint-1>0:
                last = midpoint - 1
            else:
                return midpoint
        elif cards[midpoint] < query:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return -1

for case in tests:
    answer = binary_search(case["input"]["cards"], case["input"]["query"])
    print(f"Looking for {case['input']['query']} in {case['input']['cards']}")
    print(f"Expecting {case['output']}, got {answer}")

"""
Time Complexity O(logn)
Space complexity O(n)
"""
