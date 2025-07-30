MAX_R = 2000
OFFSET = 1000

x1, y1, x2, y2 = map(int, input().split())
x1, y1 = x1 + OFFSET, y1 + OFFSET
x2, y2 = x2 + OFFSET, y2 + OFFSET

x3, y3, x4, y4 = map(int, input().split())
x3, y3 = x3 + OFFSET, y3 + OFFSET
x4, y4 = x4 + OFFSET, y4 + OFFSET

a1, b1, a2, b2 = map(int, input().split())
a1, b1 = a1 + OFFSET, b1 + OFFSET
a2, b2 = a2 + OFFSET, b2 + OFFSET

grid = [[0] * (MAX_R + 1) for i in range(MAX_R + 1)]

for i in range(x1, x2):
    for j in range(y1, y2):
        grid[i][j] = 1

for i in range(x3, x4):
    for j in range(y3, y4):
        grid[i][j] = 1

for i in range(a1, a2):
    for j in range(b1, b2):
        grid[i][j] = 0

min_x = min(x1, min(x2, (min(x3, x4))))
max_x = max(x1, max(x2, (max(x3, x4))))
min_y = min(y1, min(y2, (min(y3, y4))))
max_y = max(y1, max(y2, (max(y3, y4))))

area = 0

for i in range(min_x, max_x):
    for j in range(min_y, max_y):
        if grid[i][j] == 1:
            area += 1

print(area)