n = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if first_cards[i] > second_cards[j]:    # win
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + second_cards[j]
        else:                                   # lose, draw
            dp[i][j] = 0

print(max(map(max, dp)))