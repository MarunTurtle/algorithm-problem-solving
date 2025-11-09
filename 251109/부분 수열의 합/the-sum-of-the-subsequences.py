n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [float('-inf')] * (m + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(m, -1, -1):
        if j >= arr[i]:
            if dp[j - arr[i]] == float('-inf'):
                continue
            dp[j] = max(dp[j], dp[j - arr[i]] + 1)


print('Yes' if dp[-1] != float('-inf') else 'No')