n, m, r, c = map(int, input().split())
directions = list(input().split())
grid = [[0]*n for _ in range(n)]
r -= 1
c -= 1

front, right, bottom = 2, 3, 6

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
dirs = {
    'L': 0,
    'R': 1,
    'U': 2,
    'D': 3
}

def move_dice_cross(dir):
    global front, right, bottom
    if dir == "L":
        front, right, bottom = front, bottom, 7 - right
    elif dir == "R":
        front, right, bottom = front, 7 - bottom, right 
    elif dir == "U":
        front, right, bottom = bottom, right, 7 - front
    else:
        front, right, bottom = 7 - bottom, right, front 

def get_dice_num(d):
    if d == 'L':
        move_dice_cross('L')
        return bottom
    if d =='R':
        move_dice_cross('R')
        return bottom
    if d == 'U':
        move_dice_cross('U')
        return bottom
    if d == 'D':
        move_dice_cross('D')
        return bottom

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

grid[r][c] = bottom

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