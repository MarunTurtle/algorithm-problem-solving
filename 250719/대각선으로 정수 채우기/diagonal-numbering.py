n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

cnt = 1
for s in range(n + m - 1):  # s = i + j
    for i in range(s + 1):
        j = s - i
        if 0 <= i < n and 0 <= j < m:
            matrix[i][j] = cnt
            cnt += 1

for row in matrix:
    print(*row)