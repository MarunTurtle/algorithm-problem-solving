secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Mission:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

mission1 = Mission(secret_code, meeting_point, time)

print(f'secret code : {mission1.secret_code}')
print(f'meeting point : {mission1.meeting_point}')
print(f'time : {mission1.time}')