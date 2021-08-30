# new class
class User:
    pass

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default value
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1

# # defining attributes on the object instead of the class
# user_1.id = "001"
# user_1.username = "Bob"

user_1 = User("001", "Bob")  # Have to provide values or class won't create
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)