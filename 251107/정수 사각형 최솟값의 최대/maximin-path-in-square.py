import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
MAX_INT = sys.maxsize
value = [[MAX_INT] * n for _ in range(n)]

def initialize():
    value[0][0] = grid[0][0]
    for i in range(1, n):
        value[0][i] = min(grid[0][i], value[0][i-1])
        value[i][0] = min(grid[i][0], value[i-1][0])

initialize()

for r in range(1, n):
    for c in range(1, n):
        top = value[r-1][c]
        left = value[r][c-1]
        value[r][c] = min(max(top, left), grid[r][c])

print(value[n-1][n-1])