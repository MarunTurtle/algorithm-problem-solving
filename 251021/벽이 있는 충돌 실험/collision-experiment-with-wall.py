T = int(input())

d_map = {
    "U": 0,
    'R': 1,
    "D": 2,
    'L': 3,
}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def move(r, c, d):
    nr = r + dr[d]
    nc = c + dc[d]
    if in_range(nr, nc):
        return nr, nc, d
    else:
        return r, c, (d + 2) % 4

def simulate(grid):
    tmp_grid = [['O']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 'O':
                r, c, d = move(i, j, grid[i][j])
                if tmp_grid[r][c] != 'O':                   
                    tmp_grid[r][c] = 'O'
                else:
                    tmp_grid[r][c] = d
    return tmp_grid
                
# Simulation 
for i in range(T):
    n, m = map(int, input().split())
    grid = [['O']*n for _ in range(n)]
    for j in range(m):
        ri, ci, di = input().split()
        grid[int(ri)-1][int(ci)-1] = d_map[di]
    
    # for row in grid:
    #     print(*row)
    # print("-----")

    # 한바퀴 돌기
    for k in range(2*n):
        grid = simulate(grid)
        # for row in grid:
        #     print(*row)
        # print("-----")
        
    print(sum(1 if grid[i][j] != 'O' else 0 for i in range(n) for j in range(n)))
