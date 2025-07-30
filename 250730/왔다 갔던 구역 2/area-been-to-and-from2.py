from collections import Counter

N = int(input())
pos = 0
cnt = Counter()

for _ in range(N):
    x, d = input().split()
    x = int(x)
    if d == 'R':
        for _ in range(x):
            seg = (pos, pos + 1)
            seg = tuple(sorted(seg))
            cnt[seg] += 1
            pos += 1
    else:
        for _ in range(x):
            seg = (pos, pos - 1)
            seg = tuple(sorted(seg))
            cnt[seg] += 1
            pos -= 1

print(sum(1 for v in cnt.values() if v >= 2))
