x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

commands = list(input())
cur_dir = 0

def rotate(command):
    global cur_dir
    if command == 'L':
        cur_dir = (cur_dir + 3) % 4
    else:
        cur_dir = (cur_dir + 1) % 4

for command in commands:
    if command == 'F':
        x += dx[cur_dir]
        y += dy[cur_dir]
    else:
        rotate(command)

print(x, y)