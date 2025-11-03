from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

shelters = []
humans = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            humans.append((i, j))
        elif grid[i][j] == 3:
            shelters.append((i, j))

# 멀티소스 BFS: 모든 대피소에서 동시에 시작
dist = [[-1] * n for _ in range(n)]
q = deque()

for sr, sc in shelters:
    dist[sr][sc] = 0
    q.append((sr, sc))

drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

while q:
    r, c = q.popleft()
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] != 1 and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

# 정답 행렬: 사람 위치에는 가장 가까운 대피소까지 거리, 그 외엔 0 유지
ans = [[0] * n for _ in range(n)]
for r, c in humans:
    ans[r][c] = dist[r][c]  # 갈 수 없으면 -1이 들어감

for row in ans:
    print(*row)
