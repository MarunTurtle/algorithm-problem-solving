from collections import Counter

n = int(input())
position = 0
cnt = Counter()

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == 'L':
        for i in range(x):
            segment = (position, position - 1)
            segment = tuple(sorted(segment))
            cnt[segment] += 1
            position -= 1
    if direction == 'R':
        for i in range(x):
            segment = (position, position + 1)
            segment = tuple(sorted(segment))
            cnt[segment] += 1
            position += 1
    
ans = sum(1 for v in cnt.values() if v >= 2)

print(ans)