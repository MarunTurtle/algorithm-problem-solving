import sys
input = sys.stdin.readline

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

need = [[True] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if j == k or i == j:
                continue

            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                sys.exit(0)

            if dist[i][j] == dist[i][k] + dist[k][j]:
                need[i][j] = False
                need[j][i] = False

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if need[i][j]:
            ans += dist[i][j]

print(ans)
