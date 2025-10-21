n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def swap(r, c, nr, nc):
    tmp = grid[r][c]
    grid[r][c] = grid[nr][nc]
    grid[nr][nc] = tmp

def find_max(r, c):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    max_v = 0
    max_pos = (0, 0)
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if in_range(nr, nc): 
            if grid[nr][nc] > max_v:
                max_v = grid[nr][nc]
                max_pos = (nr, nc)
    
    return max_pos

def simulate(r, c):
    mr, mc = find_max(r, c)
    swap(r, c, mr, mc)

def find_turn(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return i, j

for t in range(m):
    for num in range(1, (n*n)+1):
        r, c = find_turn(num)
        simulate(r, c)

for row in grid:
    print(*row)