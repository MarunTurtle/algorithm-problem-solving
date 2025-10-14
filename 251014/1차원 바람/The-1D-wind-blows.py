n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def shift(r, d):
    if d == 'L':
        tmp = grid[r][m-1]
        for i in range(m-1, 0, -1):
            grid[r][i] = grid[r][i-1]
        grid[r][0] = tmp
    else:
        tmp = grid[r][0]
        for i in range(0, m-1):
            grid[r][i] = grid[r][i+1]
        grid[r][m-1] = tmp

def has_same_col_val(r1, r2):
    for i in range(m):
        if grid[r1][i] == grid[r2][i]:
            return True
    return False


def opposite(d):
    return 'L' if d == 'R' else 'R'

def propagate(start_r, start_dir):
    stack = [(start_r, start_dir, -1)]
    while stack:
        r, d, parent = stack.pop()

        u = r-1
        drow = r+1

        if u >= 0 and u != parent and has_same_col_val(r, u):
            nd = opposite(d)
            shift(u, nd)
            # for row in grid:
            #     print(*row)
            # print("======")
            stack.append((u, nd, r))
        
        if drow < n and drow != parent and has_same_col_val(r, drow):
            nd = opposite(d)
            shift(drow, nd)
            # for row in grid:
            #     print(*row)
            # print("======")
            stack.append((drow, nd, r))

for r, d in winds:
    shift(r-1, d)
    # for row in grid:
    #     print(*row)
    # print("======")
    propagate(r-1, d)

for row in grid:
    print(*row)
# print("======")