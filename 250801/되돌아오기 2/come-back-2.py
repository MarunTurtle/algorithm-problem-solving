commands = list(input())
n = len(commands)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0
x, y = 0, 0
ans = -1
time = 0

def move(command):
    global x, y
    global dir_num, time

    if command == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    elif command == 'L':
        dir_num = (dir_num + 3) % 4
    elif command == 'R':
        dir_num = (dir_num + 1) % 4
    time += 1
    if x == 0 and y == 0:
        return True
    
    return False

for command in commands:
    if move(command):
        ans = time
        break

print(ans)