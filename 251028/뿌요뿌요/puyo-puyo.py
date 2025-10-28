n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

popped = []
visited = [[0] * n for _ in range(n)]
k = 0
count = 0

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c]

def dfs(r, c):
    global count
    count = 1
    stack = [(r, c)]
    visited[r][c] = 1
    
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if can_go(nr, nc) and grid[nr][nc] == k:
                visited[nr][nc] = 1
                count += 1
                stack.append((nr, nc))

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            k = grid[i][j]
            dfs(i, j)
            popped.append(count)

print(sum(1 for pop in popped if pop >= 4), max(popped))
