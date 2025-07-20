n = int(input())
grid = [[0] * n for _ in range(n)]

if n % 2 == 0:
    k = 1
else:
    k = 0   

r, c = n-1, n-1

for i in range(1, (n*n)+1):
    grid[r][c] = i

    if c % 2 == k:
        if 0 <= r - 1 < n:
            r -= 1
        else:
            c -= 1
    else:
        if 0 <= r + 1 < n:
            r += 1
        else:
            c -= 1

for row in grid:
    print(*row)