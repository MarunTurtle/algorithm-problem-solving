n = int(input())
coin = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(4)] for _ in range(n + 1)]

dp[1][1] = coin[1]
dp[2][0] = coin[2]

for i in range(2, n+1):
    for k in range(4):
        if dp[i-2][k] != 0:
            dp[i][k] = max(dp[i][k], dp[i-2][k] + coin[i])
        if k and dp[i-1][k-1] != 0:
            dp[i][k] = max(dp[i][k], dp[i-1][k-1] + coin[i])

print(max(dp[n]))