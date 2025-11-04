from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())

sr -= 1; sc -= 1
er -= 1; ec -= 1

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# visited[r][c][b]: (r,c)에 벽 b개 부수고 도달했는가
visited = [[[False]*(k+1) for _ in range(n)] for __ in range(n)]

# (r, c, broken, dist)
q = deque()

# 시작점이 벽인 경우도 안전하게 처리 (가능하면 시작과 동시에 1개 부수고 시작)
visited[sr][sc][0] = True
q.append((sr, sc, 0, 0))

drs = (0, 0, -1, 1)
dcs = (1, -1, 0, 0)

ans = -1

while q:
    r, c, b, d = q.popleft()
    if (r, c) == (er, ec):
        ans = d
        break

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if not in_range(nr, nc):
            continue

        cell = grid[nr][nc]
        if cell == 0:
            if not visited[nr][nc][b]:
                visited[nr][nc][b] = True
                q.append((nr, nc, b, d+1))
        else:  # cell == 1, 벽
            if b < k and not visited[nr][nc][b+1]:
                visited[nr][nc][b+1] = True
                q.append((nr, nc, b+1, d+1))

print(ans)
