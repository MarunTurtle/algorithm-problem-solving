# N * N grid / M개의 구슬
# 상 하 좌 우 
# 충돌 시 사라짐
# T초 후 결과

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = [tuple(map(int, input().split())) for _ in range(m)]
positions = [[0] * n for _ in range(n)]

for x, y in marbles:
    positions[x-1][y-1] = 1

def move(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    max_v = 0
    ans = (0, 0)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] > max_v:
                max_v = grid[nr][nc]
                ans = (nr, nc)
    return ans

def check_marble_count():
    count = 0
    for i in range(n):
        for j in range(n):
            if positions[i][j]:
                count += 1
                # print(i, j)
    return count

def is_marble(r, c):
    return positions[r][c] == 1

# for row in positions:
#     print(*row)
# print("=====")

for i in range(t):
    next_pos = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if is_marble(i, j):
                nr, nc = move(i, j)
                next_pos[nr][nc] += 1
    
    for i in range(n):
        for j in range(n):
            if next_pos[i][j] > 1:
                next_pos[i][j] = 0
        
    positions = next_pos[:]
    # for row in positions:
    #     print(*row)
    # print("=====")


print(check_marble_count())