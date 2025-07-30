n = int(input())
MAX_R = 200
OFFSET = 100

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

area = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+8):
        for j in range(y, y+8):
            if grid[i][j] == 0:
                grid[i][j] = 1
                area += 1
            else:
                continue

print(area)