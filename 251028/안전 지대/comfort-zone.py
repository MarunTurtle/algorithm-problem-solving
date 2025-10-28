import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

K = 0
for row in grid:
    K = max(K, max(row))

dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def is_safe(r, c, k):
    return 0 <= r < n and 0 <= c < m and grid[r][c] > k

def flood_fill(sr, sc, k):
    stack = [(sr, sc)]
    visited[sr][sc] = True
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_safe(nr, nc, k) and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))

max_safe_area = 0
argmax_k = 1

for k in range(1, K):
    visited = [[False]*m for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(m):
            if is_safe(r, c, k) and not visited[r][c]:
                flood_fill(r, c, k)
                count += 1
    if count > max_safe_area:
        max_safe_area = count
        argmax_k = k

print(argmax_k, max_safe_area)
