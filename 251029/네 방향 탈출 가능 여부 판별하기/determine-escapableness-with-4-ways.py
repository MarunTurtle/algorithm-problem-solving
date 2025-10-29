from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

start = (0, 0)
end = (n-1, m-1)

visited = [[0]* m for _ in range(n)]

q = deque()

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    return in_range(r, c) and grid[r][c] and not visited[r][c]

def bfs():
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]        
            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))

visited[0][0] = 1
q.append(start)
bfs()

print(visited[n-1][m-1])
