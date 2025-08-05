n, m = map(int, input().split())

# Please write your code here.
x, y = (0, 0)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cur_dir = 0
grid = [[0] * m for _ in range(n)]
grid[x][y] = 1

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m and grid[r][c] == 0

for i in range(2, (n * m) + 1):
    while True:
        nx = x + dx[cur_dir]
        ny = y + dy[cur_dir]

        if in_range(nx, ny):
            x, y = nx, ny
            grid[x][y] = i
            break
        else:
            cur_dir = (cur_dir + 1) % 4

for row in grid:
    for num in row:
        print(num, end=" ")
    print()

    

