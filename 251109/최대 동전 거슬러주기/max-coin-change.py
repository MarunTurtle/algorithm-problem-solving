n, t = map(int, input().split())
coins = [0] + list(map(int, input().split()))

dp = [float('-inf')] * (t + 1)
dp[0] = 0

for t in range(1, t+1):
    for i in range(1, n+1):
        if t >= coins[i]:
            if dp[t - coins[i]] == float('-inf'):
                continue
            
            dp[t] = max(dp[t], dp[t - coins[i]] + 1)

print(-1 if dp[-1] == float('-inf') else dp[-1])