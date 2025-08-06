import sys
MIN_DIST = sys.maxsize

n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]

min_distance = MIN_DIST

for i in range(1, n-1):
    curr_distance = 0
    x, y = checkpoints[0][0], checkpoints[0][1]
    for j in range(1, n):
        if j == i:
            continue
        else:
            nx, ny = checkpoints[j][0], checkpoints[j][1]
            curr_distance += abs(nx - x) + abs(ny - y)
            x, y = nx, ny
            
    min_distance = min(min_distance, curr_distance)

print(min_distance)