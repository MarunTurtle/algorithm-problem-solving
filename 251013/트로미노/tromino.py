blocks = [
    [(0, 0), (0, 1), (-1, 0)],
    [(0, 0), (-1, 0), (-1, 1)],
    [(-1, 0), (-1, 1), (0, 1)],
    [(-1, 1), (0, 1), (-1, 0)],
    [(0, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (2, 0)]
]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for r in range(n):
    for c in range(m):
        for block in blocks:
            s = 0
            valid = True
            for dr, dc in block:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    s += grid[nr][nc]
                else:
                    valid = False
                    break
            if valid:
                ans = max(ans, s)

print(ans)