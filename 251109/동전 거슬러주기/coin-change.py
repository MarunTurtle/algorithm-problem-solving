# n개이 동전, target 목표 값
n, target = map(int, input().split())
coins = [0] + list(map(int, input().split()))

dp = [0] + [float('inf')] * target
for coin in coins:
    dp[coin + 1] = 1

for v in range(1, target + 1):
    for j in range(1, n + 1):
        if v >= coins[j]:
            if dp[v - coins[j]] == float('inf'):
                continue
            dp[v] = min(dp[v], dp[v - coins[j]] + 1)

print(dp)
