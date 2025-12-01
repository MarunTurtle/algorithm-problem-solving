# num of clothes, num of days
n, m = map(int, input().split())
# start, end, value
clothes = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n + 1) for _ in range(m + 1)]
for i, cloth in enumerate(clothes):
    s, e, v = cloth
    if s <= 1 and 1 <= e:
        dp[1][i+1] = v

for i in range(2, m+1):
    for j in range(1, n+1):
        if dp[i-1][j] != 0:
            for cloth in clothes:
                s, e, v = cloth
                if s <= i and i <= e:        
                    if dp[i][j] == 0:
                        dp[i][j] = v    
                    else:
                        diff = abs(dp[i-1][j] - dp[i][j])   
                        if diff <= abs(v - dp[i-1][j]):
                            dp[i][j] = v

ans = 0
for c in range(1, n+1):
    res = 0
    for r in range(2, m+1):
        res += abs(dp[r-1][c] - dp[r][c])
    ans = max(res, ans)

print(ans)