n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
ans = 0
dp = [[[] for _ in range(n+1)] for _ in range(n+1)]

dp[0][0].append(0)

def in_range(num):
    return -20 <= num <= 20

for i in range(1, n+1):
    v = nums[i]
    if len(dp[i-1][0]) != 0 and in_range(dp[i-1][0][0] + v):
        dp[i][0].append(dp[i-1][0][0] + v)

for i in range(1, n+1):
    for j in range(1, n+1):
        v = nums[i]
        if len(dp[i-1][j-1]) != 0:
            for e in dp[i-1][j-1]:
                r = e - v
                if in_range(r):
                    dp[i][j].append(r)
        if len(dp[i-1][j]) != 0:
            for e in dp[i-1][j]:
                r = e + v
                if in_range(r):
                    dp[i][j].append(r)

for col in dp[n]:
    if len(col) != 0:
        for e in col:
            if e == m:
                ans += 1 

# for row in dp:
#     print(*row)

print(ans)