from collections import deque
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N
    
def can_go(r, c, num):
    return in_range(r, c) and not visited[r][c] and grid[r][c] < num

def bfs(num, cur_pos):
    q = deque([cur_pos])
    visited[cur_pos[0]][cur_pos[1]] = True
    
    min_max = 0
    pos = [cur_pos]
    
    while q:
        cr, cc = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = cr + dr, cc + dc
            if can_go(nr, nc, num):
                q.append((nr, nc))
                visited[nr][nc] = True
                
                if grid[nr][nc] > min_max:
                    min_max = grid[nr][nc]
                    pos = [(nr, nc)]
                elif grid[nr][nc] == min_max:
                    pos.append((nr, nc))
    
    pos = sorted(pos, key = lambda x : (x[0], x[1]))
    return min_max, pos[0]
    
    
base = grid[r-1][c-1]
base_pos = (r-1, c-1)
    
for _ in range(K):
    visited = [[False for _ in range(N)] for _ in range(N)]
    base, base_pos = bfs(base, base_pos)

print(base_pos[0] + 1, base_pos[1] + 1)