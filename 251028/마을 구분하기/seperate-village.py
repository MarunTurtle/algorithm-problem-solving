n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
villages = []
villagers = 0
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n and grid[r][c]

def dfs(r, c):
    global villagers
    stack = [(r, c)]
    visited[r][c] = 1
    villagers += 1
    while stack:  
        r, c = stack.pop()      
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if in_range(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                villagers += 1
                stack.append((nr, nc))

for i in range(n):
    for j in range(n):
        villagers = 0
        if grid[i][j] and not visited[i][j]:
            dfs(i, j)
            villages.append(villagers)

villages.sort()
print(len(villages))
for village in villages:
    print(village)