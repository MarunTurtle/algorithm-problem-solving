import sys
input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# x1, x2 -> (x1, 0), (x2, 1)
# MAX_N = 100
# -1 000 000 <= x <= 1 000 000
# x1s don't overlap, x2s don't overlap

crossed = [0] * n

for i in range(n-1):
    for j in range(i+1, n):
        x1, x2 = lines[i][0], lines[i][1]
        x3, x4 = lines[j][0], lines[j][1]

        if x1 < x3:
            if x2 < x4:
                continue
            else: 
                crossed[i] = 1
                crossed[j] = 1
        else:
            if x2 > x4:
                continue
            else:
                crossed[i] = 1
                crossed[j] = 1     

ans = crossed.count(0)
print(ans)