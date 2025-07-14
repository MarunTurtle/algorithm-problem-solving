grid1 = [[x for x in map(int, input().split())] for _ in range(3)]
input()
grid2 = [[y for y in map(int, input().split())] for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(grid1[i][j] * grid2[i][j], end=" ")
    print()