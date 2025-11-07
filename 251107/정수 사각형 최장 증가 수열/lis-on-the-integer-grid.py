n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

cells = []
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort()

drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]

for value, r, c in cells:
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] > value:
            dp[nr][nc] = max(dp[nr][nc], dp[r][c] + 1)

print(max(map(max, dp)))