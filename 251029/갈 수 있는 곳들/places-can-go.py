from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

visited = [[0] * n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and grid[r][c] != 1

def bfs():
    while q:
        r, c = q.pop()
        visited[r][c] = 1
        for sr, sc in zip(dr, dc):
            nr = r + sr
            nc = c + sc
            if can_go(nr,  nc):
                q.appendleft((nr, nc))

for coord in points:
    r, c = coord
    r -= 1
    c -= 1
    q = deque()
    q.append((r, c))
    bfs()

print(sum(1 for i in range(n) for j in range(n) if visited[i][j] == 1))