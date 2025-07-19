grid1 = [list(map(int, input().split())) for _ in range(3)]
input()
grid2 = [list(map(int, input().split())) for _ in range(3)]
grid3 = [[0] * 3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        grid3[i][j] = grid1[i][j] * grid2[i][j]

for row in grid3:
    print(*row)