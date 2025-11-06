from collections import deque
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
candies = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    g[x].append(y)
    g[y].append(x)

# 1) BFS로 연결 컴포넌트 묶기 -> (그룹인원, 그룹사탕합) 리스트 생성
visited = [0] * n
groups = []

for s in range(n):
    if visited[s]:
        continue
    q = deque([s])
    visited[s] = 1
    cnt = 0
    total = 0

    while q:
        cur = q.popleft()
        cnt += 1
        total += candies[cur]
        for nx in g[cur]:
            if not visited[nx]:
                visited[nx] = 1
                q.append(nx)

    groups.append((cnt, total))  # (인원, 사탕합)

groups.sort(key=lambda x: (-x[1], x[0]))

cap = k - 1
if cap <= 0:
    print(0)
    sys.exit(0)

dp = [0] * (cap + 1)
for cnt, total in groups:
    for w in range(cap, cnt - 1, -1):
        dp[w] = max(dp[w], dp[w - cnt] + total)

print(max(dp))