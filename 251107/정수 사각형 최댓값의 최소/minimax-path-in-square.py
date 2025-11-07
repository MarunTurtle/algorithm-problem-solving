n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def initialize():
    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[0][i] = max(grid[0][i], dp[0][i-1])
        dp[i][0] = max(grid[i][0], dp[i-1][0])

initialize()

for r in range(1, n):
    for c in range(1, n):
        top = dp[r-1][c]
        left = dp[r][c-1]
        dp[r][c] = max(min(top, left), grid[r][c])

print(dp[n-1][n-1])