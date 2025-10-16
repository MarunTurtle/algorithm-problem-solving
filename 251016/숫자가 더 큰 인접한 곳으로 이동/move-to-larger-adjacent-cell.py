n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r -= 1
c -= 1

# Please write your code here.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_grid(r, c):
    return 0 <= r < n and 0 <= c < n

ans = [grid[r][c]]

def get_max_value(r, c):
    value = grid[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if in_grid(nr, nc):
            if grid[r][c] < grid[nr][nc]:
                r, c = nr, nc
                value = grid[nr][nc]
                break

    return r, c, value


while True:
    nr, nc, v = get_max_value(r, c)
    if v == grid[r][c]:
        break
    else:
        ans.append(v)
        # print(f"v: {v}")
        r, c = nr, nc
    
print(*ans)