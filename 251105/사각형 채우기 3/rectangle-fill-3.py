n = int(input())

# Please write your code here.
dp = [0] * (1000 + 2)
dp[1] = 2
dp[2] = 7
dp[3] = 22

for i in range(4, n + 1):
    dp[i] = 3 * dp[i-1] + dp[i-2] - dp[n-3]

print(dp[n] % 1000000007)