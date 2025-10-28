n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
K = 0
max_safe_area = 0
max_k = 0

for row in grid:
    K = max(K, max(row))

def is_safe(r, c, k):
    return 0 <= r < n and 0 <= c < m and grid[r][c] > k

def dfs(r, c, k):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    visited[r][c] = True
        
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if is_safe(nr, nc, k) and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, k)

for k in range(1, K):
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if is_safe(r, c, k) and not visited[r][c]:
                dfs(r, c, k)
                count += 1

    if count > max_safe_area:
        max_safe_area = count
        max_k = k

print(max_k, max_safe_area)