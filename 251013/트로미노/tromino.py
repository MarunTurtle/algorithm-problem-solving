blocks = [
    # ㄴ자 모양 (4방향)
    [(0,0),(1,0),(0,1)],
    [(0,0),(1,0),(1,1)],
    [(0,0),(0,1),(-1,1)],
    [(0,0),(0,1),(1,1)],

    # 일자 모양 (가로, 세로)
    [(0,0),(0,1),(0,2)],
    [(0,0),(1,0),(2,0)]
]

n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            s = 0
            valid = True
            for dr, dc in block:
                nr, nc = i + dr, j + dc
                if 0 <= nr < n and 0 <= nc < m:
                    s += grid[nr][nc]
                else:
                    valid = False
                    break
            if valid:
                ans = max(ans, s)

print(ans)
