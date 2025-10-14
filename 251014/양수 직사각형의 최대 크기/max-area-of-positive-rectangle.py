n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = -1

for r1 in range(n):
    for c1 in range(m):
       for r2 in range(r1, n):
            for c2 in range(c1, m):
                all_pos = True
                for i in range(r1, r2+1):
                    for j in range(c1, c2+1):
                        if grid[i][j] <= 0:
                            all_pos = False
                            break
                    if not all_pos:
                        break
                
                if all_pos:
                    v = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
                    ans = max(ans, v)

print(ans)