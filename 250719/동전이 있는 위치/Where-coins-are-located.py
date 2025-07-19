n, m = map(int, input().split())

ans = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    ans[x-1][y-1] += 1

for row in ans:
    print(*row)