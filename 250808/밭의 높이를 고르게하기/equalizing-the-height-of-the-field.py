import sys

n, h, t = map(int, input().split())
sow = list(map(int, input().split()))

min_sum = sys.maxsize

for i in range(n - t + 1):
    for j in range(i+t-1, n):
        cur_sum = 0
        for k in range(i, j+1):
            cur_sum += abs(h - sow[k])
        min_sum = min(cur_sum, min_sum)

print(min_sum)