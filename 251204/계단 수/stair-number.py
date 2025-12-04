n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(10):
        for k in range(10):
            if abs(j - k) == 1:
                dp[i][j] += dp[i-1][k]

# for row in dp:
#     print(*row)

ans = sum(dp[n])
print(ans % 1000000007)