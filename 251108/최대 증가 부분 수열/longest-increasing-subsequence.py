import sys

INT_MIN = -sys.maxsize

n = int(input())
nums = list(map(int, input().split()))

dp = [0] * n

def initialize():
    for i in range(n):
        dp[i] = INT_MIN
    
    dp[0] = 1

initialize()

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) 