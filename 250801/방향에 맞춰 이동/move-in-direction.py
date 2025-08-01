x, y = 0, 0
n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    d, moves = input().split()
    moves = int(moves)
    
    for i in range(moves):
        if d == 'E':
            x, y = x + dx[0], y + dy[0]
        elif d == 'S':
            x, y = x + dx[1], y + dy[1]
        elif d == 'W':
            x, y = x + dx[2], y + dy[2]
        else:
            x, y = x + dx[3], y + dy[3]

print(x, y)