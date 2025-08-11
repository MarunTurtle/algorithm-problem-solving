import sys

input = sys.stdin.readline

n = int(input())
coords = []

for i in range(n):
    coords.append(tuple(map(int, input().split())))

min_area = sys.maxsize

for i in range(n):
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = 0, 0
    for j in range(n):
        if j == i:
            continue
        min_x = min(coords[j][0], min_x)
        min_y = min(coords[j][1], min_y)
        max_x = max(coords[j][0], max_x)
        max_y = max(coords[j][1], max_y)

    min_area = min(min_area, ((max_x - min_x) * (max_y - min_y)))

print(min_area)
