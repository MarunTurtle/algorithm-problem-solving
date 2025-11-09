n, target = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [float('inf')] * (target + 1)
dp[0] = 0

for i in range(1, n+1):
    for j in range(target, -1, -1):
        if j >= arr[i]:
            if dp[j - arr[i]] == float('inf'):
                continue
            dp[j] = min(dp[j], dp[j - arr[i]] + 1)

print(-1 if dp[-1] == float('inf') else dp[-1])