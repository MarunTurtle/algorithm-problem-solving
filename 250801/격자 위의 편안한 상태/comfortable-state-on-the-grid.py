n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
grid = [[0] * (n + 1) for _ in range(n+1)]


def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= n

def is_safe(r, c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not in_range(nr, nc):
            continue
        else:
            if grid[nr][nc] != 1:
                continue
            else:
                cnt += 1
    if cnt == 3: 
        return True
    else:
        return False

for r, c in points:
    grid[r][c] = 1
    if is_safe(r, c):
        print(1)
    else:
        print(0)
