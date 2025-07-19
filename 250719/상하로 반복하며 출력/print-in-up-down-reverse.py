n = int(input())

cnt = 1

grid = [[0] * n for _ in range(n)]

for j in range(n):
    for i in range(n):
        if j % 2 == 0:
            grid[i][j] = cnt
        else:
            grid[i][j] = n + 1 - cnt
        if cnt == n:
            cnt = 1
        else:
            cnt += 1

print('\n'.join(''.join(map(str, row)) for row in grid))