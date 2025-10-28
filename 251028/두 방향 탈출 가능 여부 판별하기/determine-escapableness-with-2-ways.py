n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

end = (n-1, m-1)
dr = [1, 0]
dc = [0, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    return in_range(r, c) and grid[r][c] == 1

def dfs(r, c):
    grid[r][c] = 2
    
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if can_go(nr, nc):
            dfs(nr, nc)

dfs(0, 0)
print(1 if grid[n-1][m-1] == 2 else 0 )