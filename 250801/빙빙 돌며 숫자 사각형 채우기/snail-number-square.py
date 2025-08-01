n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0<= c < m

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c = 0, 0
dir_num = 1

grid[r][c] = 1

for i in range(2, n * m + 1):
    nr = r + dr[dir_num]
    nc = c + dc[dir_num]

    if not in_range(nr, nc) or grid[nr][nc] != 0:
        dir_num = (dir_num + 1) % 4

    r += dr[dir_num]
    c += dc[dir_num]
    grid[r][c] = i

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()