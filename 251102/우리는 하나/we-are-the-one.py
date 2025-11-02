from collections import deque

# N 크기의 나라
# K 개의 도시 선택
# low <= grid[r][c] <= high
n, k, low, high = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

selected_cities = []
ans = 0

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(nr, nc, cr, cc):
    return in_range(nr, nc) and low <= abs(grid[cr][cc] - grid[nr][nc]) <= high and not seen[nr][nc]
    
seen = [[0] * n for _ in range(n)]

def bfs(selected_cities):
    q = deque()
    drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]
    
    for city in selected_cities:
        cr, cc = city
        q.append(city)
        seen[cr][cc] = 1

    while q:
        cr, cc = q.popleft()    
        for dr, dc in zip(drs, dcs):
            nr = cr + dr
            nc = cc + dc
            if can_go(nr, nc, cr, cc):
                q.append((nr, nc))
                seen[nr][nc] = 1

    return sum(1 for i in range(n) for j in range(n) if seen[i][j] == 1)

def get_city_combo(selected_num_city, r, c):
    global visited, ans, seen

    if selected_num_city == k:
        seen = [[0] * n for _ in range(n)]
        pos_ans = 0
        pos_ans = bfs(selected_cities)
        ans = max(ans, pos_ans)
        return

    # 범위 벗어나면 종료
    if r == n:
        return

    # 다음 좌표 계산 (오른쪽 → 아래로)
    next_r, next_c = (r, c + 1) if c + 1 < n else (r + 1, 0)

    # 현재 칸 선택하는 경우
    if not visited[r][c]:
        visited[r][c] = 1
        selected_cities.append((r, c))

        get_city_combo(selected_num_city + 1, next_r, next_c)

        selected_cities.pop()
        visited[r][c] = 0

    # 현재 칸을 선택하지 않는 경우
    get_city_combo(selected_num_city, next_r, next_c)

get_city_combo(0, 0, 0)
print(ans)
