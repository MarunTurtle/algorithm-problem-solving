INF = -10**18

n = int(input())
cards = []
for _ in range(2 * n):
    r, b = map(int, input().split())
    cards.append((r, b))

N = 2 * n
# dp[i][r] = i번째 카드까지 고려했을 때,
#           빨강을 r번 쓴 경우의 최대 점수
dp = [[INF] * (n + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    r_val, b_val = cards[i - 1]
    for red in range(0, n + 1):
        blue = i - red
        # 파랑 개수도 0..n 범위 안이어야 함
        if blue < 0 or blue > n:
            continue

        # 이번 카드에서 빨강 선택
        if red > 0 and dp[i-1][red-1] != INF:
            dp[i][red] = max(dp[i][red], dp[i-1][red-1] + r_val)

        # 이번 카드에서 파랑 선택
        if blue > 0 and dp[i-1][red] != INF:
            dp[i][red] = max(dp[i][red], dp[i-1][red] + b_val)

ans = dp[N][n]
print(ans)
