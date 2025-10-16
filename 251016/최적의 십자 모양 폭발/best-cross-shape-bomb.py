n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def manhattan_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def explode(r, c, pwr):
    for i in range(n):
        for j in range(n):
            if manhattan_dist(r, c, i, j) < pwr and ((r == i) or (c == j)):
                grid[i][j] = 0

def gravity():
    for c in range(n):
        tmp = [0] * n
        i = n-1
        for r in range(n-1, -1, -1):
            if grid[r][c]:
                tmp[i] = grid[r][c]
                i -= 1

        for r in range(n-1, -1, -1):
            grid[r][c] = tmp[r]

def calculate_row_pair():
    total = 0
    for r in range(n):
        for c in range(n-1):
            if grid[r][c] == 0:
                continue
            if grid[r][c] == grid[r][c+1]:
                total += 1
    return total

def calculate_col_pair():
    total = 0
    for c in range(n):
        for r in range(n-1):
            if grid[r][c] == 0:
                continue
            if grid[r][c] == grid[r+1][c]:
                total += 1
    return total

def calculate():
    return calculate_row_pair() + calculate_col_pair()

max_v = 0

for r in range(n):
    for c in range(n):
        tmp_grid = [row[:] for row in grid]

        pwr = grid[r][c]
        explode(r, c, pwr)
        gravity()
        total = calculate()
        max_v = max(max_v, total)
        
        grid = [row[:] for row in tmp_grid]

# tmp_grid = [row[:] for row in grid]

# pwr = grid[2][2]
# explode(2, 2, pwr)
# gravity()

# for row in grid:
#     print(*row)
# print("=====")

# total = calculate()
# max_v = max(max_v, total)

# grid = [row[:] for row in tmp_grid]

# for row in grid:
#     print(*row)
# print("=====")

print(max_v)