MAX = 100

n = int(input())

grid = [[0] * (MAX * 2) for i in range(MAX * 2)]

cur = (MAX, MAX)

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1 + MAX, y1 + MAX
    x2, y2 = x2 + MAX, y2 + MAX

    for j in range(x1, x2):
        for k in range(y1, y2):
            grid[j][k] += 1

cnt = 0

for i in range(MAX*2):
    for j in range(MAX*2):
        if grid[i][j] >= 1:
            cnt += 1

print(cnt)