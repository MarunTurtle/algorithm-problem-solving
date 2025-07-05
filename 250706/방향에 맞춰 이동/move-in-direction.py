n = int(input())
x, y = 0, 0 

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    if c_dir == 'E':
        move_dir = 0
    elif c_dir == "W":
        move_dir = 1
    elif c_dir == "S":
        move_dir = 2
    elif c_dir == "N":
        move_dir = 3

    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)