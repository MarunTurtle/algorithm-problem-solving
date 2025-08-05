n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.
cur_dir = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = n // 2, n // 2
grid[x][y] = 1
# print(f"x:{x}, y:{y}, i:1, dir:{cur_dir}")

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def turn(nx, ny):
    if nx == n // 2 and ny == n // 2:
        return cur_dir
    elif nx == ny and nx <= n // 2 and ny <= n // 2:
        return (cur_dir + 1) % 4
    elif n - nx == ny + 1 or nx + 1 == n - ny:
        return (cur_dir + 1) % 4
    elif nx + 1 == ny and nx >= (n // 2):
        return (cur_dir + 1) % 4
    else:
        return cur_dir
    


for i in range(2, (n*n) + 1):
    cur_dir = turn(x, y)

    x += dx[cur_dir]
    y += dy[cur_dir]

    # print(f"x:{x}, y:{y}, i:{i}, dir:{cur_dir}")

    if not in_range(x, y):
        print(x, y)
        break
    grid[x][y] = i

for row in grid:
    for num in row:
        print(num, end=' ')
    print()