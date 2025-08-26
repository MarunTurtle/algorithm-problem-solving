import sys
input = sys.stdin.readline

n = int(input())
hills = [int(input()) for _ in range(n)]

min_total = sys.maxsize

for i in range(1, 84):
    total = 0
    for hill in hills:
        if i > hill:
            total += (i - hill) ** 2
        elif i + 17 < hill:
            total += (hill - i - 17) ** 2
        else:
            continue
    min_total = min(min_total, total)

print(min_total)