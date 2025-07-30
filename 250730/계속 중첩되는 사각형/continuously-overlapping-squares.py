n = int(input())

MAX_R = 200
OFFSET = 100

rects = [tuple(map(int, input().split())) for _ in range(n)]

grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = i

area = 0

for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if grid[x][y] % 2 == 0 and grid[x][y] != 0:
            area += 1

print(area)