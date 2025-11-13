n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == float('-inf'):
            continue
        value = second_cards[j] if first_cards[i] > second_cards[j] else 0
        # print(value)
        dp[i][j] = max(max(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + value

        if first_cards[i] > second_cards[j]:
            for k in range(i+1, n+1):
                dp[k][j] = float('-inf')
        else:
            for k in range(i+1, n+1):
                dp[i][k] = float('-inf')

        # for row in dp:
        #     print(*row)

print(max(map(max, dp)))