import sys
sys.setrecursionlimit(10**7)
from collections import deque  # 없어도 되지만 원래 코드 호환 위해 둠

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 증가하는 방향으로만 이동 → DAG → 메모이제이션으로 최장 증가 경로
drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

dp = [[0] * n for _ in range(n)]  # dp[r][c] = (r,c)에서 시작하는 최장 길이

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    if dp[r][c]:                # 이미 계산됨
        return dp[r][c]
    best = 1                    # 자기 자신만 포함하는 길이
    cur = grid[r][c]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] > cur:
            best = max(best, 1 + dfs(nr, nc))
    dp[r][c] = best
    return best

ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dfs(r, c))

print(ans)
