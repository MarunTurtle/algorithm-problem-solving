n, m, r, c = map(int, input().split())
directions = list(input().split())
grid = [[0]*n for _ in range(n)]
r -= 1
c -= 1

dice_cross = [
    [0, 5, 0],
    [4, 6, 3],
    [0, 2, 0]
]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dirs = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3
}

def move_dice_cross(dir):
    if dir == "L":
        dice_cross[1][2] = dice_cross[1][1]
        dice_cross[1][1] = dice_cross[1][0]
        dice_cross[1][0] = 7 - dice_cross[1][2]
    elif dir == "R":
        dice_cross[1][0] = dice_cross[1][1]
        dice_cross[1][1] = dice_cross[1][2]
        dice_cross[1][2] = 7 - dice_cross[1][0]
    elif dir == "U":
        dice_cross[2][1] = dice_cross[1][1]
        dice_cross[1][1] = dice_cross[0][1]
        dice_cross[0][1] = 7 - dice_cross[2][1]
    else:
        dice_cross[0][1] = dice_cross[1][1]
        dice_cross[1][1] = dice_cross[2][1]
        dice_cross[2][1] = 7 - dice_cross[0][1]

def get_dice_bottom():
    return dice_cross[1][1]

def get_dice_num(d):
    if d == 'L':
        move_dice_cross('L')
        return get_dice_bottom()
    if d =='R':
        move_dice_cross('R')
        return get_dice_bottom()
    if d == 'U':
        move_dice_cross('U')
        return get_dice_bottom()
    if d == 'D':
        move_dice_cross('D')
        return get_dice_bottom()

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

grid[r][c] = get_dice_bottom()

for d in directions:
    nr = r + dr[dirs[d]]
    nc = c + dc[dirs[d]]
    if in_range(nr, nc):
        r, c = nr, nc
        grid[r][c] = get_dice_num(d)
    else:
        continue

ans = sum(grid[i][j] if grid[i][j] else 0 for i in range(n) for j in range(n))

print(ans)