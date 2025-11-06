from collections import deque
import sys
input = sys.stdin.readline

n, m, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))

g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
groups = []

for s in range(1, n + 1):
    if visited[s]:
        continue
    q = deque([s])
    visited[s] = True
    cnt = 0
    tot = 0
    while q:
        cur = q.popleft()
        cnt += 1
        tot += candies[cur]
        for nx in g[cur]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
    if cnt < K:
        groups.append((cnt, tot))

dp = [0] * K
for size, val in groups:
    dp[size:K] = [max(a, b + val) for a, b in zip(dp[size:K], dp[:K - size])]

print(dp[K - 1])
