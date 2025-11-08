n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

dp[0] = 1

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))