n = int(input())
coin = [0] + list(map(int, input().split()))
NEG = -10**18
dp = [[NEG]*4 for _ in range(n+1)]
dp[0][0] = 0

for i in range(1, n+1):
    for k in range(1, 4):
        if dp[i-1][k-1] != NEG:
            dp[i][k] = max(dp[i][k], dp[i-1][k-1] + coin[i])
    if i >= 2:
        for k in range(4):
            if dp[i-2][k] != NEG:
                dp[i][k] = max(dp[i][k], dp[i-2][k] + coin[i])
    else:
        pass

ans = max(dp[n])
print(ans if ans != NEG else -1)
