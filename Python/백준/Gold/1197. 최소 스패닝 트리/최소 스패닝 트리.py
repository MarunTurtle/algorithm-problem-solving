import sys
import heapq

input = sys.stdin.buffer.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a].append((w, b))
    adj[b].append((w, a))

visited = [False] * (V + 1)
hq = [(0, 1)]  
mst_sum = 0
picked = 0

while hq and picked < V:
    w, u = heapq.heappop(hq)
    if visited[u]:
        continue
    visited[u] = True
    mst_sum += w
    picked += 1
    for nw, v in adj[u]:
        if not visited[v]:
            heapq.heappush(hq, (nw, v))

print(mst_sum)
