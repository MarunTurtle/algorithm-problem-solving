import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_dist = sys.maxsize

def squared(x, y):
    return (x - y)**2

for i in range(n-1):
    for j in range(i+1, n):
        dist = squared(points[i][0], points[j][0]) + squared(points[i][1], points[j][1])
        min_dist = min(min_dist, dist)

print(min_dist)