from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    cur_val = grid[r][c]
    best_val = -1
    best_pos = (r, c)

    q = deque()
    visited = [[False]*n for _ in range(n)]

    q.append((r, c))
    visited[r][c] = True  

    while q:
        x, y = q.popleft()
        for dx, dy in zip(drs, dcs):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] < cur_val:
                visited[nx][ny] = True
                q.append((nx, ny))
                val = grid[nx][ny]
                if (val > best_val or
                    (val == best_val and (nx, ny) < best_pos)):
                    best_val = val
                    best_pos = (nx, ny)
    return best_pos

for _ in range(k):
    nr, nc = bfs()
    r, c = nr, nc

print(r + 1, c + 1)
