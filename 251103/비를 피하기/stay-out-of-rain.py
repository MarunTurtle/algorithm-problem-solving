from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shelters = []
humans = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            humans.append((i, j))
        elif grid[i][j] == 3:
            shelters.append((i, j))
        else:
            continue

drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]
ans = [[0] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c, visited):
    return in_range(r, c) and not visited[r][c] and grid[r][c] != 1

def bfs(human):

    paths = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque([human])

    while q:
        r, c = q.popleft()
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc, visited):
                visited[nr][nc] = 1
                paths[nr][nc] = paths[r][c] + 1
                q.append((nr, nc))
                if grid[nr][nc] == 3:
                    break

    min_value = float('inf')

    for shelter in shelters:
        sr, sc = shelter
        if paths[sr][sc]:
            min_value = min(min_value, paths[sr][sc])
    
    if min_value == float('inf'):
        min_value = - 1
    
    ans[human[0]][human[1]] = min_value

for human in humans:
    bfs(human)

for row in ans:
    print(*row)
