n = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1

dr = [-1, -1,  0, 1, 1, 1,  0, -1]
dc = [ 0,  1,  1, 1, 0, -1, -1, -1]

ans = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_max(x, y, cnt):
    global ans
    if cnt > ans:
        ans = cnt

    d = move_dir[x][y] - 1  # 0-index 방향
    cx, cy = x, y
    # 해당 방향으로 직선상 모든 칸을 스캔하며, 값이 더 큰 칸으로만 이동
    while True:
        cx += dr[d]
        cy += dc[d]
        if not in_range(cx, cy):
            break
        if grid[cx][cy] > grid[x][y]:
            find_max(cx, cy, cnt + 1)

find_max(r, c, 0)
print(ans)
