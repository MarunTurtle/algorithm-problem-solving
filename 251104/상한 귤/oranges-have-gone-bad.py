from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = [[-1] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

bad_fruits = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            bad_fruits.append((i, j))
            visited[i][j] = 1
            result[i][j] = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

q = deque(bad_fruits)
drs, dcs = [0, 0, -1 ,1], [-1, 1, 0, 0]

while q:
    r, c = q.popleft()
    
    for dr, dc in zip(drs, dcs):
        nr = r + dr
        nc = c + dc
        if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc]:
            visited[nr][nc] = 1
            result[nr][nc] = result[r][c] + 1
            q.append((nr, nc))

for i in range(n):
    for j in range(n):
        if result[i][j] == -1 and grid[i][j] == 1:
            result[i][j] = -2

for row in result:
    print(*row)