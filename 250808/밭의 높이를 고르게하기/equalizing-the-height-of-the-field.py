import sys

n, h, t = map(int, input().split())
sow = list(map(int, input().split()))

min_sum = sys.maxsize

for i in range(n - t + 1):
    cur_sum = 0
    for j in range(i, i+t):
        cur_sum += abs(h - sow[j])
    min_sum = min(cur_sum, min_sum)

print(min_sum)