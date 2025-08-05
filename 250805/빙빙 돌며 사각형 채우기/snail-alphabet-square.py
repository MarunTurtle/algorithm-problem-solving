n, m = map(int, input().split())

base = 65

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cur_dir = 0

grid = [[0] * m  for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m and grid[r][c] == 0

x, y = 0, 0
grid[0][0] = 'A'

for i in range(2, (n*m) + 1):
    letter = chr(base + i - 1)
    
    while True:
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]
        
        if in_range(nx, ny):
            x += dx[cur_dir]
            y += dy[cur_dir]
            grid[x][y] = letter
            break
        else:
            cur_dir = (cur_dir + 1) % 4

for row in grid:
    for a in row:
        print(a, end=" ")
    print()