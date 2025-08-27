import sys 

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

def is_possible():
    for i in range(n):
        min_v = sys.maxsize
        max_v = 0
        for j in range(n):
            if j == i:
                continue
            min_v = min(x2[j], min_v)
            max_v = max(x1[j], max_v)
        
        if min_v <= max_v:
            return True
    return False

if is_possible():
    print('Yes')
else:
    print('No')