n, m = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(n)]
grid2 = [list(map(int, input().split())) for _ in range(n)]
grid3 = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            grid3[i][j] = 0
        else:
            grid3[i][j] = 1

for row in grid3:
    print(*row)