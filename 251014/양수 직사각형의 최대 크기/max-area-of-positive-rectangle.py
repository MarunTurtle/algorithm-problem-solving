n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

mask = [[1 if grid[i][j] > 0 else 0 for j in range(m)] for i in range(n)]

prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = (
            mask[i-1][j-1]
            + prefix[i-1][j]
            + prefix[i][j-1]
            - prefix[i-1][j-1]
        )

max_area = -1
for r1 in range(1, n + 1):
    for r2 in range(r1, n + 1):
        for c1 in range(1, m + 1):
            for c2 in range(c1, m + 1):
                total = (
                    prefix[r2][c2]
                    - prefix[r1-1][c2]
                    - prefix[r2][c1-1]
                    + prefix[r1-1][c1-1]
                )
                area = (r2 - r1 + 1) * (c2 - c1 + 1)

                # 모든 원소가 양수인 경우
                if total == area:
                    max_area = max(max_area, area)

print(max_area)
