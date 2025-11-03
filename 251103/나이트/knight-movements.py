from collections import deque

n = int(input())
sr, sc, er, ec = map(int, input().split())
steps = [[-1] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def can_go(r, c):
    return in_range(r, c) and not visited[r][c]

q = deque()
drs, dcs = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

def push(r, c, new_step):
    steps[r][c] = new_step
    visited[r][c] = 1
    q.append((r, c))

def bfs():
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                push(nr, nc, steps[r][c] + 1)

push(sr-1, sc-1, 0)
bfs()
print(steps[er-1][ec-1])