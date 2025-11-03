from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
score = [[0] * m for _ in range(n)]

# Please write your code here.
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    return in_range(r, c) and grid[r][c] and not visited[r][c]

q = deque()
drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]

def push(r, c, value):
    score[r][c] = value
    visited[r][c] = 1
    q.append((r, c))

def bfs():
    while q:
        (r, c) = q.popleft()        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                push(nr, nc, score[r][c] + 1)

push(0, 0, 0)
bfs()

print(score[n-1][m-1] if score[n-1][m-1] else -1)