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
        pass

    def find(self, username):
        pass

    def update(self, user):
        pass

    def listall(self):
        pass


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]



