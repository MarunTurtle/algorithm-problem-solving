n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

for i in range(1, n):
    for j in range(i):
        if j + arr[j] >= i:
            if j == 0 or dp[j] != 0:
                dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))