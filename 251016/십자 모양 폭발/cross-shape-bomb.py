n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
d = grid[r-1][c-1]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 범위 내 있는지 확인하는 함수
def in_grid(r, c):
    return 0 <= r < n and 0 <= c < n

# 현재 위치 = 폭탄이 터진 위치
cur_r, cur_c = r-1, c-1

# print(f"r, c = {cur_r}, {cur_c}")

def explode(cur_r, cur_c, d):
    global grid

    for i in range(4):
        for j in range(d):
            nr = cur_r + (dr[i] * j)
            nc = cur_c + (dc[i] * j)
            if in_grid(nr, nc):
                # print(f"nr, nc = {nr}, {nc}")
                grid[nr][nc] = 0
            else:
                break

def gravity(grid): 
    for c in range(n):
        tmp = []
        for r in range(n):
            if grid[r][c] != 0:
                tmp.append(grid[r][c])
        l = len(tmp)
        for r in range(n-1, n-l-1, -1): # l = 2, n = 5 -> 4, 2
            grid[r][c] = tmp.pop()
        for r in range(n-l-1, -1, -1): # 2, -1
            grid[r][c] = 0

        



# 그리드를 보면서 중력 시뮬레이션 가동
    # 모든 COLUMN을 보면서
        # 남아있는 숫자들 TMP에 담고
        # 기존 컬럼을 재할당

explode(cur_r, cur_c, d)
gravity(grid)

for row in grid:
    print(*row)