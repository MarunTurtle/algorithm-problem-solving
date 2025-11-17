n = int(input())
coins = [0] + list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(4)]

dp[1][1] = coins[1]
if n > 1:
    dp[2][0] = coins[2]
    dp[2][2] = coins[1] + coins[2]

for i in range(3, n+1):
    for j in range(4):
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i])
        if j and dp[i-1][j-1] != 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i])

print(max(dp[n]))