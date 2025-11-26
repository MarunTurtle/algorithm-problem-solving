MOD = 10**9 + 7
MAXN = 1005

n = int(input())

dp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(MAXN)]

dp[1][1][0] = 1  
dp[1][0][1] = 1  
dp[1][0][0] = 1  

for i in range(1, n):
    for j in range(3):
        for k in range(3):

            dp[i + 1][j + 1][0] = (dp[i + 1][j + 1][0] + dp[i][j][k]) % MOD

            dp[i + 1][j][0] = (dp[i + 1][j][0] + dp[i][j][k]) % MOD

            if k < 2:
                dp[i + 1][j][k + 1] = (dp[i + 1][j][k + 1] + dp[i][j][k]) % MOD

ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k]) % MOD

print(ans)
