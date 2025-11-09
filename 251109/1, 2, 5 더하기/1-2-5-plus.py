n = int(input())
nums = [0, 1, 2, 5]
dp = [0] * (n + 1)
for num in nums:
    dp[num] = 1
dp[0] = 0
for i in range(1, n+1):
    for j in range(1, 4):
        if i >= nums[j]:
            if dp[i - nums[j]] == 0:
                continue
            dp[i] += dp[i - nums[j]]

print(-1 if dp[-1] == 0 else dp[-1])
