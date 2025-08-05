n, m = map(int, input().split())

# Please write your code here.
x, y = (0, 0)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cur_dir = 0
grid = [[0] * m for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m and grid[r][c] == 0

for i in range(1, (n * m) + 1):
    grid[x][y] = i

    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]

    if in_range(nx, ny):
        x, y = nx, ny
    else:
        cur_dir = (cur_dir + 1) % 4
        x += dx[cur_dir]
        y += dy[cur_dir]

for row in grid:
    for num in row:
        print(num, end=" ")
    print()

    

