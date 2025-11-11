n = int(input())
coin = [0] + list(map(int, input().split()))
dp = [float('-inf')] * (n+1)
ones = [0] * (n+1)
cnt = 0
dp[1] = 0

for i in range(2, n+1):
    if ones[i-1] == 3:
        dp[i] = dp[i-2] + coin[i]
        ones[i] = ones[i-2]
    else:
        if dp[i-1] > dp[i-2]:
            ones[i] = ones[i-1] + 1
            dp[i] = dp[i-1] + coin[i]
        else:
            ones[i] = ones[i-2]
            dp[i] = dp[i-2] + coin[i]

print(dp[-1] if dp[-1] != float('-inf') else -1)