n, m, q = map(int, input().split())

# Create 2D array for building state
grid = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# 범위 확인
def in_pos(r1, c1, r2, c2, r, c): 
    return r1 <= r <= r2 and c1 <= c <= c2

# 시계 방향으로 도는 함수
def rotate(r1, c1, r2, c2):
    end_value = grid[r1+1][c1]
    length = ((r2 - r1 + 1) * 2) + ((c2 - c1 + 1) * 2) - 4

    cd = 0
    cur_r, cur_c = r1+1, c1
    for i in range(length-1):
        nr = cur_r + dr[cd]
        nc = cur_c + dc[cd]
        if not in_pos(r1, c1, r2, c2, nr, nc):
            cd = (cd + 1) % 4
            nr = cur_r + dr[cd]
            nc = cur_c + dc[cd]
        grid[cur_r][cur_c] = grid[nr][nc]
        cur_r, cur_c = nr, nc
    
    grid[r1][c1] = end_value


# 주변 평균을 반환하는 함수
def get_average(r, c, grid):
    total = grid[r][c]
    dividend = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            total += grid[nr][nc]
            dividend += 1
    return total // dividend
    

# 모든 바람 마다
    # 시작점과 끝점 설정
    # 시계방향으로 돌리고
    # 시작점 - 끝점 모든 원소를 주변 평균값으로 변환
for r1, c1, r2, c2 in winds:
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    rotate(r1, c1, r2, c2)
    
    tmp_grid = [[0]*m for _ in range(n)]
    # 건물 상태 출력 
    for i in range(n):
        for j in range(m):
            tmp_grid[i][j] = grid[i][j]

    for i in range(n):
        for j in range(m):
            if r1 <= i <= r2 and c1 <= j <= c2:
                grid[i][j] = get_average(i, j, tmp_grid)
            else:
                grid[i][j] = tmp_grid[i][j]
    
# 건물 상태 출력
for row in grid:
    print(*row)
