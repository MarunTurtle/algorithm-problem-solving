n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coins = 0

for i in range(n):
    for j in range(n-3+1):
        sum_coins = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        max_coins = max(sum_coins, max_coins)

print(max_coins)