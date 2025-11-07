import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
value = [[0] * n for _ in range(n)]

def initialize(): 
    value[0][n-1] = grid[0][n-1]
        
    for c in range(n-2, -1, -1):
        value[0][c] = value[0][c+1] + grid[0][c]

    for r in range(1, n):
        value[r][n-1] = value[r-1][n-1] + grid[r][n-1]
    
initialize()

for r in range(1, n):
    for c in range(n-2, -1, -1):
        top = value[r-1][c]
        right = value[r][c+1]
        value[r][c] = min(top, right) + grid[r][c]

print(value[n-1][0])

