n = int(input())
code = list(map(int, input().split()))

ans = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(i - code[0]) <= 2 or abs(j - code[1]) <= 2 or abs(k - code[2]) <= 2:
                ans += 1

print(ans)