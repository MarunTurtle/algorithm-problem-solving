import sys

p = list(map(int, input().split()))

def get_diff(a, b, c):
    fist_sum = p[a] + p[b] + p[c]
    sec_sum = sum(p) - fist_sum
    diff = abs(fist_sum - sec_sum)
    return diff

min_diff = sys.maxsize

for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            pos_diff = get_diff(i, j, k)
            min_diff = min(min_diff, pos_diff)

print(min_diff)