N = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
grid = [list(input()) for _ in range(N)]
s, e = x, y
s_dir = 0
# for row in grid:
#     print(*row)

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def wall_on_right(r, c, direct):
    if direct == 0:
        if r+1 < N:
            return grid[r+1][c] == '#'
        return False
    elif direct == 1:
        if c+1 < N:
            return grid[r][c+1] == '#'
        return False
    elif direct == 2:
        if r-1 >= 0:
            return grid[r-1][c] == '#'
        return False
    else:
        if c-1 >= 0:
            return grid[r][c-1] == '#'
        return False

def can_go_forward(r, c, direct):
    nr = r + dr[direct]
    nc = c + dc[direct]
    return grid[nr][nc] == '.'

def can_exit(r, c, direct):
    nr = r + dr[direct]
    nc = c + dc[direct]    
    return (nr < 0 or nr >= N) or (nc < 0 or nc >= N)

def rotate_anti_clock(direct):
    return (direct + 1) % 4

def rotate_clock(direct):
    return (direct + 3) % 4

def go_forward(r, c, direct):
    return r + dr[direct], c + dc[direct]

# case0 - 우측 벽 O, 탈출 O => 전진
# case1 - 우측 벽 O, 전진 O => 전진
# case2 - 우측 벽 O, 전진 X => direct + 1
# case3 - 우측 벽 X => direct - 1, 전진
# *case - 시작점과 direct가 같아지면 탈출 불가 -1 

count = 0
cur_direct = 0

while True:
    if wall_on_right(x, y, cur_direct):
        if can_exit(x, y, cur_direct):
            count += 1
            # print(f"can_exit: {x, y, cur_direct}")
            break
        elif can_go_forward(x, y, cur_direct):
            x, y = go_forward(x, y, cur_direct)
            count += 1
            # print(f"can go forward: {x, y, cur_direct}")
        else:
            cur_direct = rotate_anti_clock(cur_direct)
            # print(f"rotate anti clock: {x, y, cur_direct}")
    else:
        cur_direct = rotate_clock(cur_direct)
        x, y = go_forward(x, y, cur_direct)
        # print(f"rotate clock and go forward: {x, y, cur_direct}")
        count += 1
    if (x, y) == (s, e) and cur_direct == s_dir:
        count = -1
        break

print(count)