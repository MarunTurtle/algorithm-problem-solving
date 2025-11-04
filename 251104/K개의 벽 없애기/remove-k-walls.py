from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())

sr -= 1
sc -= 1
er -= 1
ec -= 1

# 벽 배열 생성
walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            walls.append((i, j))

# 선택된 벽 저장 배열 선언
selected_wall = []

# 방문 가능 여부 확인
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 정답: 도달 불가 시 -1
ans = float('inf')

# 벽 선택 이후 dfs 돌기
def bfs():
    q = deque()
    visited = [[0] * n for _ in range(n)]
    path = [[0] * n for _ in range(n)]

    q.append((sr, sc))
    visited[sr][sc] = 1
    
    drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

    while q:
        r, c = q.popleft() 
        if (r, c) == (er, ec):
            return path[r][c]
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] != 1:
                visited[nr][nc] = 1
                path[nr][nc] = path[r][c] + 1
                q.append((nr, nc))
    return float('inf')

def select_wall_get_ans(num_wall, idx):
    global ans

    if num_wall == k:
        for wall in selected_wall:
            wr, wc = wall
            grid[wr][wc] = 0
        
        dist = bfs()
        ans = min(ans, dist)

        for wall in selected_wall:
            wr, wc = wall
            grid[wr][wc] = 1
        return
    
    if idx == len(walls):
        return
    
    selected_wall.append(walls[idx])
    select_wall_get_ans(num_wall + 1, idx + 1)
    selected_wall.pop()

    select_wall_get_ans(num_wall, idx + 1)
      
select_wall_get_ans(0, 0)
print(-1 if ans == float('inf') else ans)