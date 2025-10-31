from collections import deque

n, k, bomb_count = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[0] * n for _ in range(n)]
drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c]

def bfs(start_pos):
    global bomb_count
    q = deque()
    r, c = start_pos[0] - 1, start_pos[1] - 1
    q.append((r, c))
    visited[r][c] = 1

    while q:
        cr, cc = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = cr + dr, cc + dc
            if can_go(nr, nc):
                if grid[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                else:
                    if bomb_count > 0:
                        bomb_count -= 1
                        visited[nr][nc] = 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                    else:
                        continue

for start_pos in starts:  
    bfs(start_pos)

print(sum(1 for i in range(n) for j in range(n) if visited[i][j] == 1))