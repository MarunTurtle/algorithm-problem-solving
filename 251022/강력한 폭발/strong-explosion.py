n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
bombs = []
max_bomb = 0
# Please write your code here.
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bombs.append((i, j))

m = len(bombs)

def count(grid_map):
    count = 0
    for i in range(n):
        for j in range(n):
            if grid_map[i][j] == -1:
                count += 1
    return count

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def explode(coord, v, grid):
    r, c = coord
    if v == 0:
        dr = [-2, -1, 0, 1, 2]
        dc = [0, 0, 0, 0, 0]
    elif v == 1:
        dr = [0, -1, 0, 1, 0]
        dc = [0, 0, 1, 0, -1]
    else:
        dr = [0, -1, 1, 1, -1]
        dc = [0, 1, 1, -1, -1]
    for d in range(5):
        nr = r + dr[d]
        nc = c + dc[d]
        if in_range(nr, nc):
            grid[nr][nc] = -1

def backtrack(depth, grid):
    global max_bomb
    if depth == m:
        max_bomb = max(max_bomb, count(grid))
        return

    for v in range(3):
        tmp_grid = [row[:] for row in grid]
        explode(bombs[depth], v, tmp_grid)
        backtrack(depth + 1, tmp_grid)

backtrack(0, grid)
print(max_bomb)