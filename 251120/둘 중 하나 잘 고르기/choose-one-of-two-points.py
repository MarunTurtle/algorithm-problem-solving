import sys
INT_MIN = -sys.maxsize
n = int(input())
red = [0]
blue = [0]
for i in range(2*n):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

dp = [[INT_MIN] * (n + 1) for _ in range(2*n + 1)]
dp[0][0] = 0

for i in range(1, 2*n + 1):
    for j in range(n+1):
        if abs(i - j) <= n: # 현재 라운드 갯수 - red선택한 갯수가 기준 갯수보다 같거나 작을 때
            if dp[i-1][j] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + blue[i])

            if j != 0 and dp[i-1][j-1] != INT_MIN:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + red[i])

print(max(dp[2*n]))