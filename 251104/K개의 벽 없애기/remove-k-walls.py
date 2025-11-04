from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())

sr, sc = sr - 1, sc - 1
er, ec = er - 1, ec - 1

visited = [[[0] * (k+1) for _ in range(n)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

q = deque()
drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

# r, c, broken, dist
q.append((sr, sc, 0, 0))
visited[sr][sc][0] = 1

ans = -1

while q:
    r, c, broken, dist = q.popleft()
    if (r, c) == (er, ec):
        ans = dist
        break
    
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc
        if in_range(nr, nc):
            if grid[nr][nc] == 0 and not visited[nr][nc][broken]:
                visited[nr][nc][broken] = 1
                q.append((nr, nc, broken, dist + 1))
            else:
                if broken < k and not visited[nr][nc][broken + 1]:
                    visited[nr][nc][broken + 1] = 1
                    q.append((nr, nc, broken + 1, dist + 1))

print(ans)