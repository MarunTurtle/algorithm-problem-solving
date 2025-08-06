n, m = map(int, input().split())
grid = [list(input().split()) for _ in range(n)]

# Please write your code here.

def is_jumpable(x, y, nx, ny):
    return x < nx and y < ny and grid[nx][ny] != grid[x][y]


cnt = 0
x, y = 0, 0
trgt_x, trgt_y = n-1, m-1

for i in range(1, n-1):
    for j in range(1, m-1):
        if is_jumpable(x, y, i, j):
            for k in range(i+1, n-1):
                for l in range(j+1, m-1):
                    if is_jumpable(i, j, k, l):
                        if is_jumpable(k, l, n-1, m-1):
                            # print(i, j, k, l)
                            cnt += 1

print(cnt)


