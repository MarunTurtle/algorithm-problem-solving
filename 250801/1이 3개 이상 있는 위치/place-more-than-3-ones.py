n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def count_neighbors(r, c):
    global grid

    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            if grid[nr][nc] == 1:
                cnt += 1
    return cnt

ans = 0

for i in range(n):
    for j in range(n):
        cnt = count_neighbors(i, j)
        if cnt >= 3:
            ans += 1

print(ans)