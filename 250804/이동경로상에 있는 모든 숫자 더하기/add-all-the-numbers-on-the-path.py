n, t = map(int, input().split())
commands = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# U, R, D, L
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur_dir = 0
x, y = n//2, n//2
total = grid[x][y]
# print(total)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(command):
    global x, y
    global cur_dir
    global total

    if command == 'L':
        cur_dir = (cur_dir + 3) % 4
    elif command == 'R':
        cur_dir = (cur_dir + 1) % 4
    else:
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]
        if in_range(nx, ny):
            x += dx[cur_dir]
            y += dy[cur_dir]
            total += grid[x][y]
            # print(total)

for command in commands:
    move(command)

print(total)