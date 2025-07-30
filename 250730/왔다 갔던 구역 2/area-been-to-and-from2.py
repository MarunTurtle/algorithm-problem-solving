N = int(input())
pos = 0
seg_count = {}

for _ in range(N):
    x, d = input().split()
    x = int(x)
    
    for _ in range(x):
        prev = pos
        if d == 'R':
            pos += 1
        else:
            pos -= 1
        seg = (min(prev, pos), max(prev, pos))
        seg_count[seg] = seg_count.get(seg, 0) + 1

# 2번 이상 지난 구간의 개수 출력
print(sum(1 for v in seg_count.values() if v >= 2))
