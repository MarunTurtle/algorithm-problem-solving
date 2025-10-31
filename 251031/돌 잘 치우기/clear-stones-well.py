from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
starts = [tuple(map(int, input().split())) for _ in range(k)]

drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(board):
    """모든 시작점을 동시에 넣고 멀티소스 BFS로 방문 가능한 칸 수 계산"""
    q = deque()
    visited = [[0]*n for _ in range(n)]
    for sr, sc in starts:
        r, c = sr-1, sc-1
        if not in_range(r, c): 
            continue
        if board[r][c] == 1:   # 시작점이 돌이면 진행 불가
            continue
        if not visited[r][c]:
            visited[r][c] = 1
            q.append((r, c))
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return cnt

# 돌 좌표 목록 수집
rocks = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]
t = min(b, len(rocks))

# 예외: 치울 돌이 없거나 b==0이면 바로 BFS
if t == 0:
    print(bfs(grid))
    sys.exit(0)

ans = 0

# 조합으로 t개의 돌을 선택해 제거 → BFS → 최댓값
for pick in combinations(rocks, t):
    # 보드 복사 후 선택한 돌 제거
    board = [row[:] for row in grid]
    for (r, c) in pick:
        board[r][c] = 0
    ans = max(ans, bfs(board))

print(ans)
