n, K = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
dp = [[float('-inf')] * (K+1) for _ in range(n+1)]
dp[0][0] = 0

max_ans = float('-inf')

for i in range(1, n+1):
    for k in range(K+1):
        if numbers[i] >= 0:
            if dp[i-1][k] == float('-inf'):
                continue
            else:
                dp[i][k] = dp[i-1][k] + numbers[i]
                max_ans = max(max_ans, dp[i][k])
        else:
            if k == 0:
                dp[i][k] = 0
            else:
                dp[i][k] = dp[i-1][k-1] + numbers[i]
                max_ans = max(max_ans, dp[i][k])
     
# for row in dp:
#     print(*row)

print(max_ans)