n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def get_final_row():
    for r in range(1, n):
        for c in range(k-1, k-2+m):
            if grid[r][c] == 1:
                return r - 1
    return n-1

final_row = get_final_row()

for c in range(k-1, k-1+m):
    grid[final_row][c] = 1

for row in grid:
    print(' '.join(map(str, row)))