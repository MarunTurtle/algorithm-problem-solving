n, m = map(int, input().split())
clothes = [None] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (n + 1) for _ in range(m + 1)]

for j in range(1, n+1):
    s = clothes[j][0]
    e = clothes[j][1]
    
    if s <= 1 <= e:
        dp[1][j] = 0

for i in range(2, m+1):
    for j in range(1, n+1):
        if dp[i-1][j] == -1:
            continue
        
        last_v = clothes[j][2]

        for k in range(1, n+1):
            s = clothes[k][0]
            e = clothes[k][1]

            if s <= i <= e:
                cur_v = clothes[k][2]
                dp[i][k] = max(dp[i][k], dp[i-1][j] + abs(last_v - cur_v))

print(max(dp[m]))