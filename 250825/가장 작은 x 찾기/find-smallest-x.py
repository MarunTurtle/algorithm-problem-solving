import sys

n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

ans = sys.maxsize
start = a[0] // 2
end = b[0] // 2

for i in range(start, end+1):
    pos_ans = True
    for j in range(1, n+1):
        if a[j-1] <= i * (2 ** j) <= b[j-1]:
            continue
        else:
            pos_ans = False
    if pos_ans:
        ans = i
        break

print(ans)

