n = int(input())

ans = [[1] * i for i in range(1, n+1)]

for r in range(1, n):
    for c in range(1, r):
        ans[r][c] = ans[r-1][c] + ans[r-1][c-1]

for row in ans:
    print(*row)