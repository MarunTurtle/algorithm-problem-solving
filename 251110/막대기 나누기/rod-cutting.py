n = int(input())
profit = [0] + list(map(int, input().split()))
dp = [float('-inf')] * (n+1)
dp[0] = 0

for i in range(1, n+1): # 총 막대 길이
    for j in range(1, n+1): # 선택한 막대 
        if i >= j: 
            if dp[i - j] != float('-inf'):
                dp[i] = max(dp[i], dp[i-j] + profit[j])

print(max(dp))
            
