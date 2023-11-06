"""
QUESTION 1: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure
to manage profile information (username, name and email) for 100 million users. It should allow the following
operations to be performed efficiently:

1 Insert the profile information for a new user.
2 Find the profile information of a user, given their username
3 Update the profile information of a user, given their username
4 List all the users of the platform, sorted by username

You can assume that usernames are unique.

"""

"""Problem: We need to create a data structure which can store 100 million records and perform insertion, search, 
update and list operations efficiently. """


"""Input

Key input into our data structure are user profiles, containing username, name and email

We can do this with Python Classes
"""

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name = user.name
        target.email = user.email

    def listall(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
user = database.find('siddhant')

database.insert(biraj)

# Making a Binary Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left) + TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left), [self.key], TreeNode.traverse_in_order(self.right))

    def display_keys(self, space="\t", level=0):
        # If empty node
        if self is None:
            print(space*level + "-")
            return
        # If node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left, space, level+1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return (TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right))

    def __str__(self):
        return "BinaryTree <{}?".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}?".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left(parse_tuple(data[0]))
            node.right(parse_tuple(data[2]))
        else:
            node = TreeNode(data)
        return node


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node0.key)

node0.left = node1
node0.right = node2

# tuple helper function to convert a tuple with the structure (left_subtree, key, right_subtree) into a binary tree

def parse_tuple(data):
    # isinstance() checks if the first argument is an instance of the second argument
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

# parse_tuple creates a new root node when the input tuple has three elements. Then uses recursion to make the left
# and right subtrees

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree2)
print(tree2.key)
print(tree2.left.key, tree2.right.key)
print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)
print(tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key)


def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        if node.left is None and node.right is None:
            return node.key
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))
    else:
        return None


print(tree_to_tuple(tree2))

def display_keys(node, space='\t', level=0):
    #print(node.key if node else None, level)

    #If node is empty
    if node is None:
        print(space*level + "-")
        return

    # If node is a leaf
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    # If node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


display_keys(tree2, ' ')

# inorder traversal of binary tree
def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
display_keys(tree, '  ')
print(traverse_in_order(tree))


def traverse_pre_order(node):
    if node is None:
        return []
    return([node.key] + traverse_in_order(node.left) + traverse_in_order(node.right))


def traverse_post_order(node):
    if node is None:
        return []
    return(traverse_post_order(node.left) + traverse_post_order(node.right) + [node.key])


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)



