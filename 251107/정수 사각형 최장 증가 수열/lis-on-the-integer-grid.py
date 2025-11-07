from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

visited = [[0] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]
q = deque()

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(nr, nc, r, c):
    return in_range(nr, nc) and not visited[nr][nc] and grid[r][c] < grid[nr][nc]

def initialize(sr, sc):
    for r in range(n):
        for c in range(n):
            visited[r][c] = 0
            dp[r][c] = 0
    visited[sr][sc] = 1
    dp[sr][sc] = 1
    q.append((sr, sc))

ans = 0

for sr in range(n):
    for sc in range(n):
        initialize(sr, sc)
        while q:
            r, c = q.popleft()
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if can_go(nr, nc, r, c):
                    visited[nr][nc] = 1
                    dp[nr][nc] = dp[r][c] + 1
                    q.append((nr, nc)) 
        max_value = max(map(max, dp))
        ans = max(ans, max_value)

print(ans)
        

