import sys

INT_MIN = -sys.maxsize
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

def initialize():
    for i in range(n):
        for j in range(m):
            dp[i][j] = INT_MIN
    
    dp[0][0] = 1

initialize()

for r in range(1, n):
    for c in range(1, m):
        for nr in range(r):
            for nc in range(c):                
                if dp[nr][nc] == INT_MIN:
                    continue

                if grid[r][c] > grid[nr][nc]:
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)

print(max(map(max, dp)))
