n = int(input())
# dp = [0] * (n+1)
# dp[0] = 1
# dp[1] = 1

# for i in range(2, n):
#     dp[i] = dp[i-2] + dp[i-1]

# print(dp[n-1])

memo = [-1] * (n+1)

def fibo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(n))