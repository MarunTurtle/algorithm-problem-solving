n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())
count = 0

# Down Left Up Right
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def calc_cur_place(k):
    if calc_cur_dir(k) == 0:
        return (0, k-1)
    elif calc_cur_dir(k) == 1:
        return (k-1 % n, n-1)
    elif calc_cur_dir(k) == 2:
        return (n-1, n - 1 - ((k-1) % n))
    else:
        return(n - 1 - ((k-1) % n) , 0)

def calc_cur_dir(k):
    return (k-1) // n

x, y = calc_cur_place(k)
cur_dir = calc_cur_dir(k)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def mirror_change_dir(mirror):
    global cur_dir
    global x, y
    global count

    if mirror == "\\":
        cur_dir = 3 - cur_dir
    else: # mirror == '/':
        cur_dir = cur_dir ^ 1

    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]

    count += 1
    if in_range(nx, ny):
        x, y = nx, ny
        return True
    else:
        return False

while True:
    mirror = grid[x][y]
    if mirror_change_dir(mirror):
        continue
    else:
        break

print(count)