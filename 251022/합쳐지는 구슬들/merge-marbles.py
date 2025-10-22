# 크기, 구슬 수, 시간
n, m, t = map(int, input().split())

# 구슬 보관 (순서, r, c, 방향, 무게)
marbles = []

# 격자 초기화
grid = [[[] for _ in range(n)] for _ in range(n)]

# 방향 매퍼
d_map = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}

# 방향 dr, dc
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1] 

# m개 구슬 보관 
for i in range(m):
    ri, ci, di, wi = input().split()
    marble = []
    marble.append(i+1)
    marble.append(int(ri)-1)
    marble.append(int(ci)-1)
    marble.append(d_map[di])
    marble.append(int(wi))
        
    grid[int(ri)-1][int(ci)-1].append(marble)

# ================ #
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def simulate():
    global grid

    tmp_grid = [[[] for _ in range(n)] for _ in range(n)]

    for p in range(n):
        for j in range(n):
            if grid[p][j]:
                for marble in grid[p][j]:
                    i, r, c, d, w = tuple(marble)
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if in_range(nr, nc):
                        r, c = nr, nc
                    else:
                        d = (d + 2) % 4
                    tmp_grid[r][c].append([i, r, c, d, w])
    
    for k in range(n):
        for l in range(n):
            if len(tmp_grid[k][l]) >= 2:
                max_i = -1
                total_w = 0
                max_d = -1
                for marble in tmp_grid[k][l]:
                    i, r, c, d, w = tuple(marble)
                    max_i = max(max_i, i)
                    if max_i == i:
                        max_d = d
                    total_w += w
                tmp_grid[k][l] = [[max_i, k, l, max_d, total_w]]

    grid = tmp_grid[:]

# 시간동안 simulate하기
for _ in range(t):
    simulate()

# 구슬 수, 가장 무거운 구슬의 무게 반환
max_w = 0
marble_count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            marble = grid[i][j][0]
            marble_count += 1
            max_w = max(max_w, marble[4])

# for row in grid:
#     print(*row)

print(marble_count, max_w)
