n = int(input())

# Please write your code here.
dp = [0] * (n + 2)
dp[1] = 2

for i in range(2, n + 1):
    dp[i] = (dp[i-1] * 3) + 1

print(dp[n] % 1000000007)