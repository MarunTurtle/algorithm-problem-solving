n, k = map(int, input().split())
grid = [list(map(int, list(input()))) for _ in range(n)]
changed = True

def gravity(): 
    global changed, grid
    new_board = [[0] * 10 for _ in range(n)]
    for c in range(10):
        fallen = []
        for r in range(n-1, -1, -1):
            if grid[r][c] != 0:
                fallen.append(grid[r][c])
        
        zero_needed = n - len(fallen)
        fallen += [0] * zero_needed
        
        for r in range(n-1, -1, -1):
            new_board[r][c] = fallen[n - r - 1]
            
    if new_board != grid:
        grid = new_board[:][:]
    else:
        changed = False
        
drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]
def in_range(r, c):
    return 0 <= r < n and 0 <= c < 10

def boom():
    to_boom = []
    visited = [[0] * 10 for _ in range(n)]
    def dfs(target_num, r, c, cluster):
        visited[r][c] = 1
        cluster.append((r, c))
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == target_num:
                dfs(target_num, nr, nc, cluster)

    for r in range(n):
        for c in range(10):
            if not visited[r][c] and grid[r][c]:
                target_num = grid[r][c]
                cluster = []
                dfs(target_num, r, c, cluster)
                to_boom.append(cluster)
    
    for arr in to_boom:
        if len(arr) >= k:
            for r, c in arr:
                grid[r][c] = 0
                
while changed:
    boom()
    gravity()
    
for row in grid:
    print("".join(list(map(str, row))))