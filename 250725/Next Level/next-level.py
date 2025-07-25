user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.

class Member:
    def __init__ (self, user = "codetree", lv = "10"):
        self.user = user
        self.lv = lv

user1 = Member()
user2 = Member(user2_id, user2_level)

print(f'user {user1.user} lv {user1.lv}')
print(f'user {user2.user} lv {user2.lv}')