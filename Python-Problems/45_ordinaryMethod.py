class User:
    def __init__(self, userID, userName):
        self.userId = userID
        self.userName = userName
        self.followers = 0
        self.following = 0

    def follower(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('049', "Raimal")
user_2 = User("049", 'Raimal')

# print(user_1.followers)
user_1.follower(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
