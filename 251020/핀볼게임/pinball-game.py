n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
max_count = 0

start_points = []
for i in range(n):
    start_points.append((i, 0, 0))
for i in range(n):
    start_points.append((n-1, i, 1))
for i in range(n-1, -1, -1):
    start_points.append((i, n-1, 2))
for i in range(n-1, -1, -1):
    start_points.append((0, i, 3))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def turn(cur_dir, num):
    if num == 1:
        if cur_dir == 0 or cur_dir == 2:
            return (cur_dir + 1) % 4
        if cur_dir == 1 or cur_dir == 3:
            return (cur_dir + 3) % 4
    else:
        if cur_dir == 0 or cur_dir == 2:
            return (cur_dir + 3) % 4
        if cur_dir == 1 or cur_dir == 3:
            return (cur_dir + 1) % 4        

for start_point in start_points:
    r, c, d = start_point
    # print(f"new start: {r, c}")
    count = 1
    if grid[r][c] != 0:
        d = turn(d, grid[r][c])
    while True:
        # print(f"{r, c}")
        nr = r + dr[d]
        nc = c + dc[d]
        if in_range(nr, nc):
            r, c = nr, nc
            if grid[nr][nc] != 0:
                d = turn(d, grid[nr][nc])
            count += 1
        else:
            count += 1
            # print(f"Out: {count}")
            break
    max_count = max(max_count, count)

print(max_count)