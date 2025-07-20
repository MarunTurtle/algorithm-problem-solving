n = int(input())
grid = [[1] * n for _ in range(n)]

for row in range(1, n):
    for col in range(1, n):
        grid[row][col] = grid[row-1][col] + grid[row][col-1] + grid[row-1][col-1]

for r in grid:
    print(*r)