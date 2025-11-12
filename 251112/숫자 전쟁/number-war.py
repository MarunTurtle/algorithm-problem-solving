n = int(input())
left  = list(map(int, input().split()))
right = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

# 뒤에서 앞으로 채우기
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        # 1) 왼쪽 버리기
        best = dp[i+1][j]
        # 2) 둘 다 버리기
        if dp[i+1][j+1] > best:
            best = dp[i+1][j+1]
        # 3) 왼쪽 > 오른쪽이면, 오른쪽만 버리고 점수 획득
        if left[i] > right[j]:
            cand = dp[i][j+1] + right[j]
            if cand > best:
                best = cand
        dp[i][j] = best

print(dp[0][0])
