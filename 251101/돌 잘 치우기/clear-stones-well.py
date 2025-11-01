from collections import deque
from itertools import combinations
import sys

input = sys.stdin.readline

# 입력
N, K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
starts = [tuple(map(int, input().split())) for _ in range(K)]  # 1-indexed

# 0-index로 변환
starts = [(r-1, c-1) for r, c in starts]

# 돌 좌표들 수집
stones = [(r, c) for r in range(N) for c in range(N) if board[r][c] == 1]

# 4방향
DR = (1, -1, 0, 0)
DC = (0, 0, 1, -1)

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(removed_set):
    """removed_set: 이번에 치운 돌 좌표 집합(set of (r,c))"""
    q = deque()
    visited = [[False]*N for _ in range(N)]

    # 시작점 넣기 (모두 0 위에 있다고 가정)
    for r, c in starts:
        if not visited[r][c]:
            visited[r][c] = True
            q.append((r, c))

    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for dr, dc in zip(DR, DC):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc) or visited[nr][nc]:
                continue

            cell = board[nr][nc]
            # 이동 가능 조건: 0이거나, 이번에 치운 돌
            if cell == 0 or (cell == 1 and (nr, nc) in removed_set):
                visited[nr][nc] = True
                q.append((nr, nc))

    return cnt

ans = 0

# M == 0인 경우도 커버
for removed in combinations(stones, M):
    ans = max(ans, bfs(set(removed)))

print(ans)
