n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
ans = 0
RANGE = 41 # -20 <-> 20

dp = [[0] * RANGE for _ in range(n+1)]
dp[0][20] = 1

def in_range(num):
    return 0 <= num <= 40

for i in range(1, n+1):
    v = nums[i]

    for e in range(RANGE):
        if dp[i-1][e] == 0:
            continue
        cnt = dp[i-1][e]
        
        plus_v = e + v
        if in_range(plus_v):
            dp[i][plus_v] += cnt

        minus_v = e - v
        if in_range(minus_v):
            dp[i][minus_v] += cnt
    
print(dp[n][m+20])