n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

min_v = min(x1)
max_v = max(x2)

def is_intersecting(min_v, max_v):
    for i in range(min_v, max_v + 1):
        count = 0
        for j in range(n):
            if x1[j] <= i <= x2[j]:
                count += 1
        if count == n:
            return True
    return False

if is_intersecting:
    print('Yes')
else:
    print('No')