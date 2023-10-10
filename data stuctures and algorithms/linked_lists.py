"""
How to make a linked list

1. Make a Node class
1. Add init methods
2. Make a Linked List class
3. Add init, append, show_elements, length, get_element methods
"""


class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next_node = None

    def __repr__(self):
        return f"Node data: {self.data}"


# Let's test it out

node1 = Node(2)
node2 = Node(3)
node3 = Node(5)


# print(node1, node2, node3)

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next_node != None:
                current_node = current_node.next_node
            current_node.next_node = Node(value)

    def show_elements(self):
        current_node = self.head
        while current_node != None:
            print(current_node)
            current_node = current_node.next_node

    def length(self):
        current_node = self.head
        i = 0
        while current_node != None:
            i += 1
            current_node = current_node.next_node
        return i

    def get_element(self, position):
        current_node = self.head
        i = 0
        while current_node != None:
            if position == i:
                return current_node.data
            else:
                i += 1
                current_node = current_node.next_node
        return None


print("list0")
list0 = LinkedList()
list0.show_elements()

print("list1")
list1 = LinkedList()

list1.head = Node(2)

list1.head.next_node = Node(3)

list1.head.next_node.next_node = Node(4)

list1.show_elements()

print("list2")
list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)
list2.length()
list2.show_elements()
list2.get_element(0)
list2.get_element(1)
list2.get_element(2)
list2.get_element(3)


def reverse(l):
    if l.head is None:
        return None
    current_node = l.head
    prev_node = None

    while current_node != None:
        # The idea is to use three pointers curr, prev, and next to keep track of nodes to update reverse links.
        # Track the next node. What currently is the next node will be the current mode in the next iteration
        next_node = current_node.next_node

        # Modify the current_node to point in the other direction
        current_node.next_node = prev_node

        # Update previous and current to be new. Tomorrow, the past will become the present, and present will become
        # the future.
        prev_node = current_node
        current_node = next_node
    l.head = prev_node


print("List 3")
list3 = LinkedList()
list3.append(2)
list3.append(3)
list3.append(5)
list3.append(9)
list3.show_elements()
print("Reverse List 3")
reverse(list3)
list3.show_elements()
