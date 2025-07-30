MAX_R = 2000
OFFSET = 1000

rects = [tuple(map(int, input().split())) for _ in range(2)]
grid = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

for k, (x1, y1, x2, y2) in enumerate(rects, start=1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = k

min_x, min_y = MAX_R, MAX_R
max_x, max_y = 0, 0
cnt = 0
for i in range(MAX_R + 1):
    for j in range(MAX_R + 1):
        if grid[i][j] == 1:
            if i <= min_x:
                min_x = i
            if i >= max_x:
                max_x = i
            if j <= min_y:
                min_y = j
            if j >= max_y:
                max_y = j
            cnt += 1

if cnt == 0:
    print(0)
else: 
    area = ((max_x+1) - min_x) * ((max_y+1) - min_y)
    print(area)