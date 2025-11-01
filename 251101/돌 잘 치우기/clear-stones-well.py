from collections import deque

n, num_starts, num_bomb = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
start_points = []
for _ in range(num_starts):
    r, c = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    start_points.append((r, c))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] == 0

visited = [[0] * n for _ in range(n)]

def bfs():
    global visited
    visited = [[0] * n for _ in range(n)]
    q = deque()
    for (r, c) in start_points:
        q.append((r, c))
    
    xds, yds = [0, 0, -1, 1], [-1, 1, 0, 0]

    while q:
        x, y = q.popleft()

        for xd, yd in zip(xds, yds):
            nx = x + xd
            ny = y + yd
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))

stones = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
ans = 0
selected_stones = []

def get_stone_combo_and_min_max(selected, idx):
    global ans

    if selected == num_bomb:
        for (x, y) in selected_stones:
            grid[x][y] = 0
        
        bfs()
        
        sub_ans = sum(1 for i in range(n) for j in range(n) if visited[i][j])

        ans = max(ans, sub_ans)
        # if ans == sub_ans:
            # print(ans)
            # print(selected_stones)
            # for row in grid:
            #     print(*row)
            # print("======")
    
        for (x, y) in selected_stones:
            grid[x][y] = 1
        
        return
    
    if idx == len(stones):
        return 

    selected_stones.append(stones[idx])
    get_stone_combo_and_min_max(selected + 1, idx + 1)

    selected_stones.pop()
    get_stone_combo_and_min_max(selected, idx + 1)

get_stone_combo_and_min_max(0, 0)
print(ans)