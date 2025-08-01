x, y = 0, 0
n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    d, moves = input().split()
    moves = int(moves)
    
    if d == 'E':
        move_dir = 0
    elif d == 'S':
        move_dir = 1
    elif d == 'W':
        move_dir = 2
    else:
        move_dir = 3
    
    x += dx[move_dir] * moves
    y += dy[move_dir] * moves

print(x, y)